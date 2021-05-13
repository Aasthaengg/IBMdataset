import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
s = 0
t = 0
cur = 0
ans = 0
while s < N:
    while t < N and cur + A[t] == cur ^ A[t]:
        cur += A[t]
        t += 1
    ans += t - s
    cur -= A[s]
    s += 1
print(ans)
