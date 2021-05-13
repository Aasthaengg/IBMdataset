n=input()
t=[int(i) for i in input().split()]
m=int(input())
for i in range(m):
    a,b=map(int,input().split())
    ans=t[a-1]
    t[a-1]=b
    print(sum(t))
    t[a-1]=ans