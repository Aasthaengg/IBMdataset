from itertools import combinations_with_replacement as comb_rplc
n,m,q = map(int, input().split())
arr = []

for i in range(q):
  arr.append(list(map(int, input().split())))
  
score_max = 0
for seq in comb_rplc(range(1, (m+1)), n):
  score = 0
  
  for a,b,c,d in arr:
    if seq[b-1]-seq[a-1] == c:
      score += d
      
  if score > score_max:
    score_max = score
    
print(score_max)