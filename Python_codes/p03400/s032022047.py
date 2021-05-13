n=int(input())
d,x=map(int,input().split())
ans=0
for i in range(n):
    cnt=0
    a=int(input())
    for l in range(100):
        aa=a*l+1
        if aa<=d:
            cnt+=1
        else:
            break
    #print(cnt)
    ans+=cnt
print(ans+x)