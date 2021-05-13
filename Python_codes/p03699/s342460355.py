n = int(input())
s = [int(input()) for _ in range(n)]
score = sum(s)
ans = float('inf')
if score % 10 == 0:
  for i in s:
    if i%10 != 0:
      ans = min(ans, i)
  if ans == float('inf'):
    ans = 0
    score = 0
  score -= ans
print(score)
