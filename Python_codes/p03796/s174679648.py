N=int(input())
p=1
m=10**9+7
for i in range(N):
    p=p*(i+1)
    p=p%m
print(p)