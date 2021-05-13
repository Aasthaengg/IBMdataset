a =list('CODEFESTIVAL2016')
b=list(input())
ans=int()
for i in range(16):
    if a[i]!=b[i]:
        ans+=1
print(ans)