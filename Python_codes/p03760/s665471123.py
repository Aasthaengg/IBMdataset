O=input()
E=input()
ans=[]
for m in range(len(O)+len(E)):
    ans.append('k')
for i in range(len(O)):
    ans[2*i]=O[i]
for j in range(len(E))   :
    ans[2*j+1]=E[j]

ans=''.join(ans)
print(ans)