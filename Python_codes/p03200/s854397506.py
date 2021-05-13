s = input()
n = len(s)
b_count = 0
score = 0
for i in range(n-1, -1, -1):
  if s[i] == "B":
    score += n-1-i-b_count
    b_count += 1
print(score)