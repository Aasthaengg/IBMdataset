from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))

sA = sorted(A)
l = sA[N//2 - 1]
r = sA[N//2]

median = defaultdict(int)
m = N // 2 - 1
for i,a in enumerate(sA):
  if i <= m and not median[a]:
    median[a] = sA[m+1]
  elif m < i and not median[a]:
    median[a] = sA[m]

ans = []
for a in A:
  ans.append(median[a])
  
print("\n".join(map(str,ans)))