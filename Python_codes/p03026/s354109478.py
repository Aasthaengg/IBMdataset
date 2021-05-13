
def input_from_console():
    n = int(input())
    a_list, b_list = [], []
    for i in range(n - 1):
        data = input()
        a, b = map(int, data.split())
        if b > a:
            a, b = b, a  # swap smaller one.
        a_list.append(a)
        b_list.append(b)
    c_list = list(map(int, input().split()))
    return n, a_list, b_list, c_list


def solve(n, a_list, b_list, c_list):
    edge = [[] for i in range(n)]  # 0 based list of list.
    for i in range(len(a_list)):
        a, b = a_list[i] - 1, b_list[i] - 1  # convert to 0 based index.
        edge[a].append(b)
        edge[b].append(a)
    c_list.sort(reverse=True)

    vertices = [None] * n
    vertices[0] = c_list.pop(0)

    graph_value = sum(c_list)  # edge should have the value except the maximum.

    search_path = []
    search_path.extend(edge[0])

    while search_path:
        node = search_path.pop(0)
        if vertices[node] is None:
            vertices[node] = c_list.pop(0)
            search_path.extend(edge[node])
    return "{:d}\n{}".format(graph_value, ' '.join(map(str, vertices)))


def main():
    n, a_list, b_list, c_list = input_from_console()
    print(solve(n, a_list, b_list, c_list))


if __name__ == "__main__":
    import sys

    if sys.gettrace():  # Check if the python interpreter is in debug mode or not.
        check_cases()
    else:
        main()
