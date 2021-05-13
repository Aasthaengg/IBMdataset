import bisect
n,k = map(int,input().split())
x = list(map(int,input().split()))
zero = bisect.bisect(x,0)
left = [0] + (x[:zero])[::-1]
right = [0] + x[zero:]
ans = 10**12
for i in range(min(k+1,len(left))):
  j = k-i
  if j >= len(right):
    continue
  ans = min(ans,2*right[j]-left[i],-2*left[i]+right[j])
print(ans)