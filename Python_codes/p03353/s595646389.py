s=str(input())
k=int(input())
ans=[]
for i in range(len(s)):
    for j in range(i+1,i+k+1):
        ans.append(s[i:j])
#print(ans)
ans=sorted(list(set(ans)))
#print(ans)
print(ans[k-1])
