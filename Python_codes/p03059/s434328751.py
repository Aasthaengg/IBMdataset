a,b,t=map(int,input().split())
ans=0
for i in range(1,t+100):
    if i*a>t:
        break
    else:
        ans+=b
print(ans)