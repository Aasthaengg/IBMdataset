S = input()
 
answer = "Good"
prev_s = S[0]
for s in S[1:]:
  if prev_s == s:
    answer = "Bad"
    break
  prev_s = s
 
print(answer)