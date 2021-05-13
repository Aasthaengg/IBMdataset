n,k = map(int,input().split())
p = n % k
m = n % k - k
print(min(p,-m))