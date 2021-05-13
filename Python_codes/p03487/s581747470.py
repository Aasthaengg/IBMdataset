from collections import Counter
n=int(input())
sc=Counter(list(map(int,input().split())))
sm=0
for k,v in sc.items():
  sm+=min(v,(v-k if v-k>=0 else 10**9+1)) 
print(sm)