a=list(map(int,input().split()))
k=int(input())
u=max(a)
for i in range(k):
    u=u*2
print(sum(a)-max(a)+u)