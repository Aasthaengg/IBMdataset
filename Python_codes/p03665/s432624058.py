n,p = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
for a in A:
    if a%2==0: cnt += 1
if n == cnt:
    if p == 0: ans = 2**n
    else: ans = 0
else: ans = 2**(n-1)
print(ans)