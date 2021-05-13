n=int(input())
s=input()
w=s.count(".")
ans=w
b=0
for i in range(n):
    if s[i]=="#":
        b+=1
    else:
        w-=1
    ans=min(ans,b+w)
print(ans)