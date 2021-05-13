K, X = map(int, input().split())

if X+K-1 <= 1000000:
  right = X+K-1
else:
  right = 1000000
  
if X-K+1 >= -1000000:
  left = X-K+1
else:
  left = -1000000
  
ans = [i for i in range(left, right+1)]
print(' '.join(map(str, ans)))