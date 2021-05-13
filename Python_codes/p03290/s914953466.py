D,G = map(int,input().split())
questions = [list(map(int,input().split())) for _ in range(D)]
ans = float('inf')
for bit in range(1 << D):
  count = 0
  score = 0
  max_zero_index = 0
  for i in range(D):
    if (bit >> i) & 1:
      score += questions[i][0]*100*(i+1)+questions[i][1]
      count += questions[i][0]
    else:
      max_zero_index = i
  if score >= G:
    ans = min(count,ans)
  else:
    for _ in range(1,questions[max_zero_index][0]):
      count +=1
      score += 100*(max_zero_index+1)
      if score >= G:
        ans = min(count,ans)
print(ans)