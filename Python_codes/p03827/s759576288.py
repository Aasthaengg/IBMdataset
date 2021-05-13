n=int(input())
s=input()
a=0
ans=0
for i in range(n):
    if s[i]=="I":
        a+=1
    else:
        a-=1
    ans=max(a,ans)
print(ans)