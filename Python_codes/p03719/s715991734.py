nl = lambda: list(map(int, input().split()))
sl = lambda: input().split()
n = lambda: int(input())
s = lambda: input()

A, B, C = nl()
if A <= C and C <= B:
    print('Yes')
else:
    print('No')
