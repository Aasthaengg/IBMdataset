def solve():
  ans = float('inf')
  N = int(input())
  A = list(map(int, input().split()))
  if A[0]==0:
    lis = [1,-1]
  else:
    lis = [A[0],-A[0]//abs(A[0])]
  for l in lis:
    cnt = abs(A[0]-l)
    total = l
    for i in range(1,N):
      new_total = total+A[i]
      if total*(new_total)>=0:
        new_total = (-1)*total//abs(total)
        cnt += abs(new_total-(total+A[i]))
      total = new_total
    ans = min(ans,cnt)
  return ans
print(solve())