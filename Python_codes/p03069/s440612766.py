n=int(input())
s=list(input())
b2=s.count("#")
w2=s.count(".")
b1=0
w1=0
ans=w2
for i in range(n):
    if s[i]=="#":
        b1+=1
        b2-=1
    else:
        w1+=1
        w2-=1
    ans=min(ans,b1+w2)
print(ans)
