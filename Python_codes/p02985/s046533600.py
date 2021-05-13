#!/usr/bin/env python3
import sys
MOD = 1000000007  

def solve(N: int, K: int, a: "List[int]", b: "List[int]"):
    matrix = [[] for _ in range(N+1)]
    for i in range(N-1):
        matrix[a[i]].append(b[i])
        matrix[b[i]].append(a[i])
    
    visited = [0]*(N+1)

    from collections import deque
    queue = deque()
    visited[1]=1
    answer = K
    num = K-1
    for node in matrix[1]:
        answer *= num
        answer %= MOD

        num -= 1
        queue.append(node)

    while queue:
        q = queue.popleft()
        if visited[q] != 0:
            continue
        visited[q] = 1

        num = K-2
        for child_node in matrix[q]:
            if visited[child_node] == 0:
                answer *= num
                answer %= MOD
                num -= 1
                queue.append(child_node)
        answer %= MOD

    print(answer%MOD)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    a = [int()] * (N - 1)  # type: "List[int]"
    b = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, K, a, b)

if __name__ == '__main__':
    main()
