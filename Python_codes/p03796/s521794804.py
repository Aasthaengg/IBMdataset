N=int(input())
div=10**9+7
a=1
for i in range(1, N+1):
    a=(a*i)%div
print(a)
