n=int(input())
p=1
q=10**9+7
for i in range(1,n+1):
    p=((p%q)*(i%q))%q
print(p)