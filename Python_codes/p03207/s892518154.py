n=int(input())
ans=[]
for i in range(n):
    s=int(input())
    ans.append(s)
t=max(ans)
t//=2
print(sum(ans)-t)
