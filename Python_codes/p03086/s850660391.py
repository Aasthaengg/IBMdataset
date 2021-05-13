import sys
readline = sys.stdin.readline

S = readline().rstrip()

right = 0
ans = 0
for left in range(len(S)):
  while right + 1 < len(S) and S[right] in "ACGT":
    right += 1
    
  if right + 1 == len(S):
    if S[right] in "ACGT" and ans < right - left + 1:
      ans = right - left + 1
      break
  
  if ans < right - left:
    ans = right - left
    
  if right == left:
    right += 1
    
print(ans)