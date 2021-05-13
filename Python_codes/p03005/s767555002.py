n,k = map(int,input().split())
print(max((n % k - n // k + 1),0))