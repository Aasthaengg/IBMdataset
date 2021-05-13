import bisect

N = int(input())
parts = [[] for i in range(3)]
con = [0] * N

ans = 0

for i in range(3):
  t = sorted(list(map(int,input().split())))
  parts[i] = t

under =parts[2]
middle = parts[1]
upper = parts[0]

for i in range(N):
  p = middle[i]
  ans += bisect.bisect_left(upper,p) * (N - bisect.bisect_right(under,p))
    
print(ans)