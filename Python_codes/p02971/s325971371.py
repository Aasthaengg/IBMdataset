N = int(input())
A = [int(input()) for a in range(N)]
maxnum = max(A)
maxcount = A.count(maxnum)
s = sorted(A,reverse=True)

if maxcount == 1:
  index = A.index(maxnum)
  ans = [maxnum] * N
  ans[index] = s[1]
else:
  ans = [maxnum] * N
for a in ans:
  print(a)