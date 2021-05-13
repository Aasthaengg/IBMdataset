from collections import deque
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# Aの総和 = Cの総和
p = []
cnt_p = 0
cnt_m = 0
x = 0
for a,b in zip(A,B):
    if a > b:
        cnt_p += 1
        p.append(a-b)
    elif a < b:
        cnt_m += 1
        x += b-a

if cnt_m==0:
    print(0)
    exit()

p = deque(sorted(p)[::-1])
while p and x > 0:
    P = p.popleft()
    if P <= x: x -= P
    else: x = 0
if x == 0:
    print(cnt_m+cnt_p-len(p))
else:
    print(-1)