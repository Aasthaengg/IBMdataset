n = int(input())

a = list(map(int,input().split()))

memo = [0]*n

memo[0] = 1000

for i in range(1,n):
    memo[i] = max((memo[i-1]%a[i-1]+a[i]*(memo[i-1]//a[i-1])),memo[i-1])

print(memo[-1])