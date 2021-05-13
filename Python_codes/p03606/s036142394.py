n=int(input())
person=[]
ans=0
for i in range(n):
    tmp=list(map(int,input().split()))
    ans+=tmp[1]-tmp[0]+1
print(ans)
