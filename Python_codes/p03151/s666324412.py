def solve():
  N = int(input())
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))
  C = [a-b for a,b in zip(A,B)]
  if sum(C)<0:
    return -1
  c = sum([-a for a in C if a<0])
  C.sort(reverse=True)
  ans = 0
  for i in range(N):
    if C[i]<0:
      ans += 1
      continue
    if C[i]==0 or c==0:
      continue
    c = max(c-C[i],0)
    ans += 1
  return ans
print(solve())