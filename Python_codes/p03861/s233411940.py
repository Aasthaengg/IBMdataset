a,b,x=map(int,input().split())
num_a=a//x
num_b=b//x
ans=num_b-num_a
if a%x==0:
    ans+=1
print(ans)