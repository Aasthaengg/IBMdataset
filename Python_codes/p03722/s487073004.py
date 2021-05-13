from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import bellman_ford, NegativeCycleError
import sys
buf = sys.stdin.buffer


def main():
    n, m = map(int, buf.readline().split())
    ABC = map(int, buf.read().split())

    edges = []
    routes = [[] for _ in range(n)]
    rev_routes = [[] for _ in range(n)]

    def get_reachable_nodes(start, routes):
        seen = {start}
        todo = []
        for to in routes[start]:
            todo.append(to)
            seen.add(to)

        while todo:
            node = todo.pop()
            for to in routes[node]:
                if to in seen:
                    continue
                todo.append(to)
                seen.add(to)
        return seen

    for node1, node2, value in zip(ABC, ABC, ABC):
        node1, node2 = node1 - 1, node2 - 1
        edges.append([node1, node2, -value])
        routes[node1].append(node2)
        rev_routes[node2].append(node1)

    from_start = get_reachable_nodes(0, routes)
    to_goal = get_reachable_nodes(n-1, rev_routes)
    from_start_to_goal = from_start & to_goal

    values = []
    rows = []
    cols = []

    for row, col, minus_value in edges:
        if {row, col} <= from_start_to_goal:
            values.append(minus_value)
            rows.append(row)
            cols.append(col)

    graph = coo_matrix((values, (rows, cols)), shape=(n, n))
    try:
        bf = bellman_ford(graph, indices=[0])
        print(-int(bf[0][n - 1]))
    except NegativeCycleError:
        print("inf")


if __name__ == "__main__":
    main()
