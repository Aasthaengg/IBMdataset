H, N = map(int,input().split())
C = list(map(int,input().split()))
s = 0
for i in range(N):
    s += C[i]
r = H - s
if r <= 0:
    print('Yes')
else:
    print('No')