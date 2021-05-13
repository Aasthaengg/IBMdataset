s = list(input())

answer = 0
for i in range(len(s)):
  j = len(s) - i - 1
  if (i < j) and (s[i] != s[j]) :
    answer += 1
    
print(answer)