n = int(input())
score = []
for i in range(n):
  a,b = map(int,input().split())
  score.append([a,b])
sorted_score = sorted(score, key=lambda x: x[0]+x[1], reverse=True)
i=0
t_score = 0
a_score = 0
for i,scores in enumerate(sorted_score):
  if i%2==0:
    t_score+=scores[0]
  else:
    a_score+=scores[1]
print(t_score-a_score)
    
  
