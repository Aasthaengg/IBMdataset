s=str(input())
ans=1000
for i in range(1,len(s)-1):
    x=int(s[i-1]+s[i]+s[i+1])
    if abs(x-753)<ans:
        ans=abs(x-753)
print(ans)