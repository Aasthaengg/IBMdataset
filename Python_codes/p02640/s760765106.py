import sys

input = sys.stdin.readline

n, l = list(map(int, input().split()))

t = (l//2) - n
c = (l//2) - (2*t)

if l % 2 == 1:
    print("No")
elif t < 0 or c < 0:
    print("No")
elif t > n or c > n:
    print("No")
elif t + c != n:
    print("No")
else:
    print("Yes")
