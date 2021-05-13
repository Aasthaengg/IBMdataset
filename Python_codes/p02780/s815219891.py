n,k = map(int,input().split())
p = list(map(int,input().split()))
p.append(0)
s = sum(p[:k])
t = 0
for i in range(k-1,n):
    t = max(t,(k+s)/2)
    s -= p[i-k+1]
    s += p[i+1]
print(t)