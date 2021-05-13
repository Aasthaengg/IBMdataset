#coding: UTF-8
n = int(input())
S = list(map(int,input().split()))
q = int(input())
T = list(map(int,input().split()))
ans = 0
def linsearch(v,S):
  for w in S:
    if v == w:
      return True
  return False
  
for v in T:
  if linsearch(v,S):
    ans += 1
  
print(ans)
