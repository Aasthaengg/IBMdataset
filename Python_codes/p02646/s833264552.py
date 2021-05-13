A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

lange = abs(B - A)
s = V - W

res = 0

if s != 0:
    tmp = lange / s
    if tmp <= T and tmp >= 0:
        res = 1

if (res == 0):
    print("NO")
else:
    print("YES")