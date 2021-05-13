nl = lambda: list(map(int, input().split()))
sl = lambda: input().split()
n = lambda: int(input())
s = lambda: input()

A, B, C = nl()

if C <= A+B:
    print('Yes')
else:
    print('No')
