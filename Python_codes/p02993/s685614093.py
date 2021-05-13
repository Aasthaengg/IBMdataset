s = list(input())
i = 0
answer = "Good"

while i < 3:
  if s[i] == s[i + 1]:
    answer = "Bad"
  i += 1
print(answer)