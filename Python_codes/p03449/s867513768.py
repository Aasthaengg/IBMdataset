n=int(input())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
ans=0
for i in range(n):
    num=sum(a1[:i+1])+sum(a2[i:])
    if ans<num:
        ans=num
print(ans)
