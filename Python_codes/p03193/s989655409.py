N,H,W = (int(x) for x in input().split())
A = []
B = []
for i in range(N):
    a,b = (int(x) for x in input().split())
    A.append(a)
    B.append(b)

num = []

for i in range(N):
    if A[i] >= H:
        num.append(i)

l = len(num)
ans = 0
for i in range(l):
    if B[num[i]] >= W:
        ans += 1

print(ans)