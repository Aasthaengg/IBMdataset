import sys

N = int(input())
c = list(input())

right_R = N
for i in range(N-1,-1,-1):
    if c[i] == 'R':
        right_R = i
        break

left_W = -1
for i in range(N):
    if c[i] == 'W':
        left_W = i
        break

if right_R == N or left_W == -1:
    print(0)
    sys.exit(0)

ans = 0
p = left_W
q = right_R
while p < q:
    for i in range(p+1,N):
        if c[i] == 'W':
            p = i
            break
        if i == N-1:
            p = N
    for i in range(q-1,-1,-1):
        if c[i] == 'R':
            q = i
            break
        if i == 0:
            q = -1
    ans += 1

print(ans)