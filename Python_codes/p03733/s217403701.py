N,T= map(int,input().split())
t = [int(j) for j in input().split()]
ans =T
b = 0
for i in t:
    ans+=min(i-b,T)
    b = i
print(ans)