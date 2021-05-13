nl = lambda: list(map(int, input().split()))
sl = lambda: input().split()
n = lambda: int(input())
s = lambda: input()

A, B = nl()
if B % A == 0:
    print(A+B)
else:
    print(B -A)
