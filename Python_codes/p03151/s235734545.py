def solve():
  N = int(input())
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))
  C = []
  for a,b in zip(A,B):
    C.append(a-b)
  if sum(C)<0:
    return -1
  minus = sum([abs(x) for x in C if x<0])
  ans = len([abs(x) for x in C if x<0])
  C.sort(reverse=True)
  for i in range(N):
    if minus==0:
      break
    if C[i]>0:
      ans += 1
      if minus>C[i]:
        minus -= C[i]
      else:
        minus = 0
  return ans
print(solve())