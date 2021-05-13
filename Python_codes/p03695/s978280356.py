N = int(input())
A = list(map(int,input().split()))
out = [0]*9
for i in range(N):
    if A[i]>=3200:
        out[8] += 1
    else:
        out[A[i]//400]=1
MIN = sum(out[0:8])
MAX = MIN + out[8]
if MIN>=1:
    print(MIN, MAX)
else:
    print(1,MAX)