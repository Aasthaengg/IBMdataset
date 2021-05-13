n,k = map(int,input().split())
p = list(map(int,input().split()))
ans = 0
for i in range(n):
    p[i] = (p[i] + 1)/2
ev = sum(p[:k])
if n == k:
    print(sum(p))
    exit()
for i in range(n - k):
    ev += (p[i + k] - p[i])
    ans = max(ans,ev)
print(ans)



    
