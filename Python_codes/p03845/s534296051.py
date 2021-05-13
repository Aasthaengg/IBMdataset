n=int(input())
t=[0]+list(map(int, input().split()))
m=int(input())

S=sum(t)

for i in range(m):
    p, x=map(int, input().split())
    dif=x-t[p]
    print(S+dif)