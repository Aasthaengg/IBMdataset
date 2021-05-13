N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
D = []
ans = 0
for i in range(N):
    D.append(A[i]-B[i])
DMINUS = list(filter(lambda x: x < 0,D))
ans += len(DMINUS)
MINUSSUM = sum(DMINUS)
DPULUS = sorted(filter(lambda x: x > 0,D),key=lambda x: -x)
for d in DPULUS:
    if MINUSSUM >= 0:
        break
    MINUSSUM += d
    ans += 1
if MINUSSUM < 0:
    print(-1)
else:
    print(ans)