n,k = map(int, input().split())
pn = list(map(int, input().split()))
qn = [(i+1)/2 for i in pn]
ans = sum(qn[:k])
t=ans
for i in range(1, n-k+1):
    t +=-qn[i-1]+qn[i+k-1]
    ans = max(ans, t)
print(ans)