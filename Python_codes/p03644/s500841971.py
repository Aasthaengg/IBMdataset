n=int(input())
anslist=[1,2,4,8,16,32,64]
ans=0
for i in anslist:
    if n>=i:
        ans=i
print(ans)