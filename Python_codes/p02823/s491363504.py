def solve():
  N, A, B = map(int, input().split())
  if (A-B)%2==0:
    return abs(A-B)//2
  ans = min((B+A-1)//2,N-(A+B-1)//2)
  return ans
print(solve())