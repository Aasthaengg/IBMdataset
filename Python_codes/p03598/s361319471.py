n=int(input())
k=int(input())
a=list(map(int,input().split()))

cost=0
for i in range(n):
    cost+=min(abs(a[i]),abs(k-a[i]))

print(cost*2)