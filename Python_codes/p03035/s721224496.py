import sys 
 
A, B = map(int, input().split())
cond_older = (12 < A)
cond_young = (6 <= A) & (12 >= A)
 
ans = (
  B if cond_older else
  B//2 if cond_young else
  0
)
 
print(ans)