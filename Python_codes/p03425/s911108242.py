from itertools import combinations
n=int(input())
name=[0]*5
march=['M','A','R','C','H']
for i in range(n):
  s=input()
  if s[0] in march:
    name[march.index(s[0])]+=1
sm=0
for i,j,k in list(combinations(name,3)):
  sm+=i*j*k
print(sm)