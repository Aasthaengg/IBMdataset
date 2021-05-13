n, k = map(int, input().split())  
n = n % k
while (n > abs(n-k) ):
    n = abs(n-k)
print(n)