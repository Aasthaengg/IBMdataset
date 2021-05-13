s=input()
k=int(input())
n=len(s)
ans=[]
for i in range(n):
    for j in range(1,k+1):
        if i+j<=n:
            ans.append(s[i:i+j]) 
ans=sorted(list(set(ans)))
print(ans[k-1])