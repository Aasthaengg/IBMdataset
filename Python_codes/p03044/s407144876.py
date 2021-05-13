from sys import stdin
input = stdin.buffer.readline

def main():
    n = int(input())

    edges = [[] for _ in range(n)]
    for _ in range(n-1):
        u, v, w = map(int, input().split())
        edges[u-1].append((v-1, w%2))
        edges[v-1].append((u-1, w%2))

    ans = [-1] * n
    ans[0] = 0
    todo = [0]
    while len(todo) > 0:
        parent = todo.pop(-1)
        color = ans[parent]

        for child, w in edges[parent]:
            if ans[child] == -1:
                if w == 0:
                    ans[child] = color
                else:
                    ans[child] = 1 - color
                todo.append(child)

    for i in ans:
        print(i)

main()