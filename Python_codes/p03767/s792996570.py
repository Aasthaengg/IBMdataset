N=int(input())
a=list(map(int,input().split()))
a.sort()
sum = 0
for i in range(N):
    sum += a[N+2*i]
print(sum)