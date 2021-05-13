from collections import Counter

s=input()
n=len(s)
v=n*(n-1)//2
for i in Counter(s).values():
  v-=i*(i-1)//2
print(v+1)