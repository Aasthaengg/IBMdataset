import sys
input = sys.stdin.readline

N, C = map(int, input().split())
xv = [tuple(map(int, input().split())) for _ in range(N)]
left = [0]
av = 0

for x, v in xv:
    av += v
    left.append(av-2*x)

right = [0]
av = 0

for x, v in xv[::-1]:
    av += v
    right.append(av-2*(C-x))

for i in range(1, N+1):
    left[i] = max(left[i], left[i-1])
    right[i] = max(right[i], right[i-1])

ans = 0
av = 0

for i in range(N):
    av += xv[i][1]
    ans = max(ans, av-xv[i][0]+right[N-1-i])

av = 0

for i in range(N):
    av += xv[N-1-i][1]
    ans = max(ans, av-(C-xv[N-1-i][0])+left[N-1-i])

print(ans)