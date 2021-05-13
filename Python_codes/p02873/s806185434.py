import numpy as np
s = list(input())

judge = 0
judge_min = 0
base = np.zeros(len(s))
for i in range(len(s)):
  if s[-(i+1)] == ">":
    judge += 1
    base[-(i+1)] = judge
  elif s[-(i+1)] == "<":
    judge = 0

ans = 0
if base[0] > 0:
  ans = base[0]
  temp = base[0]
elif base[0] == 0:
  ans = 0
  temp = 0
  
for i in range(1,len(s)):
  if (s[i-1] == ">") and (s[i] == ">"):
    temp = base[i]
  elif (s[i-1] == "<") and (s[i] == "<"):
    temp += 1
  elif (s[i-1] == ">") and (s[i] == "<"):
    temp = 0
  elif (s[i-1] == "<") and (s[i] == ">"):
    temp += 1
    if temp < base[i]:
      temp = base[i]
      
  ans += temp
  
  if (temp > base[i]) and (s[i] == ">"):
    temp -= 1
  
if s[-1] == "<":
  ans += temp+1

print(int(ans))