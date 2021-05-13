import collections

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = [A[0] % M]
for i in range(1, N):
    B.append((B[i-1] + A[i] % M) % M)
 
c = collections.Counter(B)
ans = sum([x*(x-1)//2 for x in c.values()])
if 0 in c.keys():
    ans += c[0]
print(ans)