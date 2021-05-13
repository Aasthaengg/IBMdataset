def solve():
  N = int(input())
  ans = [0]
  if N%2==0:
    for i in range(1,N+1):
      for j in range(i+1,N+1):
        if i+j!=N+1:
          ans[0] += 1
          ans.append(' '.join([str(i),str(j)]))
  else:
    for i in range(1,N):
      for j in range(i+1,N):
        if i+j!=N:
          ans[0] += 1
          ans.append(' '.join([str(i),str(j)]))
    for i in range(1,N):
      ans[0] += 1
      ans.append(' '.join([str(N),str(i)]))
  return ans
print(*solve(),sep='\n')