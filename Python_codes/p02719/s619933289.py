n,k = map(int, input().split())
r = n % k
s = abs(r - k)
print(min(r,s))