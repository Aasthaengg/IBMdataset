n = int(input())
a = list(map(int,input().split()))

mod = 10**9 + 7

lis = [abs(n-2*i-1) for i in range(n)]

a.sort()
lis.sort()

print(pow(2, n//2, mod)) if a==lis else print(0) 