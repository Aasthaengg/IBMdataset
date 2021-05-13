from collections import Counter
N,M = map(int,input().split())
A = list(map(int,input().split()))
B = [0]
if len(A)==1:
    print(1 if A[0]%M==0 else 0)
    exit()
else:
    for a in A:
        B.append((B[-1]+a)%M)
c = Counter(B)
ans = 0
for v in c.values():
    ans += v*(v-1)//2
print(ans)
