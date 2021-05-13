nl = lambda: list(map(int, input().split()))
sl = lambda: input().split()
n = lambda: int(input())
s = lambda: input()

A, B = nl()

print(max(A+B, A-B, A*B))
