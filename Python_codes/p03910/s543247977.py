def solve():
  cnt = 0
  N = int(input())
  ans = []
  for i in range(1,N+2):
    cnt += i
    ans.append(i)
    if cnt>N:
      ans.remove(cnt-N)
    if cnt>=N:
      break
  return ans
print(*solve(),sep='\n')