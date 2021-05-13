import sys
input = sys.stdin.readline


def get_node_count(n):
    sum = 0
    for i in range(10**6):
        sum += i
        if sum == n:
            return i+1
        if sum > n:
            return False


def main():
    n = int(input())
    k = get_node_count(n)
    if not k:
        print("No")
        return

    nodes = [[] for _ in range(k)]
    edges = []
    dup_num = 1
    for from_ in range(k-1):
        for to in range(from_+1, k):
            edge = (from_, to, dup_num)
            edges.append(edge)
            dup_num += 1

    for from_, to, num in edges:
        nodes[from_].append(num)
        nodes[to].append(num)

    print("Yes")
    print(k)
    for node in nodes:
        print(k-1, *node)


if __name__ == "__main__":
    main()
