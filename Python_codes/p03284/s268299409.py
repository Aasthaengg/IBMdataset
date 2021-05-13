n,k = map(int, input().split())
rem=n%k
print(1 if rem != 0 and rem < k else 0)
