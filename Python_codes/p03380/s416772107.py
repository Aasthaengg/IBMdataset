from bisect import bisect_left

n = int(input())
A=  list(map(int,input().split()))
A.sort()
am = A[-1]
amin = 0
ans = 0
for a in A[:-1]:
  if min(a, am-a) > amin:
    amin = min(a,am-a)
    ans = a
    
print(am , ans)