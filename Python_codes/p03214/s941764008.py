def solve():
  N = int(input())
  A = list(map(int, input().split()))
  ave = sum(A)/N
  B = list(map(lambda x:abs(x-ave),A))
  for i in range(N):
    B[i] = [B[i],i]
  B.sort(key=lambda x:(x[0],x[1]))
  ans = B[0][1]
  return ans
print(solve())