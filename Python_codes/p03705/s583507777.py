N, A, B = map(int, input().split())
Mi = (N-1)*A+B
Ma = (N-1)*B+A
ans = Ma - Mi + 1
if ans < 0:
  ans = 0
print(ans)