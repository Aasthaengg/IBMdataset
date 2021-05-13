n = int(input())
x=0
s=input()
ans=0
for i in range(n):
    if s[i]=="I":
        x=x+1
    else:
        x=x-1
    ans=max(ans,x)
print(ans)