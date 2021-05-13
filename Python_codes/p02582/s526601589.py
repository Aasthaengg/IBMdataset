S = list(input())
temp_ans = 0
ans = 0
for i in range(3):
  if S[i] == 'R':
    temp_ans += 1
  else:
    if ans < temp_ans:
      ans = temp_ans
      temp_ans = 0
else:
  if ans < temp_ans:
    ans = temp_ans
      
print(ans)