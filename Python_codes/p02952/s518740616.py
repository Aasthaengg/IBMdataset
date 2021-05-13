N=int(input())
ans=0
for i in range(N+1):
    if 1<=i<10: ans+=1
    elif 100<=i<1000: ans+=1
    elif 10000<=i<100000:  ans+=1
print(ans)

