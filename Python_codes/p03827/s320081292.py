n = int(input())
s = input()

ans = 0
score = 0
for i in range(n):
  if s[i] == "I":
    score += 1
  if s[i] == "D":
    score -= 1
  ans = max(ans, score)
  
print(ans)