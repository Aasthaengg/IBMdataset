n=int(input())
t=[0]+list(map(int,input().split()))
ans=sum(t)
o=ans
for i in range(int(input())):
    p,x=map(int,input().split())
    print(ans-t[p]+x)