ans=n=int(input())
s=input()
a=[0]
for i in s:
    if i==".":a+=[a[-1]+1]
    else:a+=[a[-1]]
w=s.count(".")
for i in range(n+1):
    ans=min(ans,i-a[i]+w-a[i])
print(ans)