def check(score):
  if score >= 3200:
    return -1
  for i,rating in enumerate(scores):
    if rating[0] <= score <= rating[1]:
      return i
n = int(input())
a = list(map(int,input().split()))
thopes = 0
colors = set()
scores = [(1,399),(400,799),(800,1199),(1200,1599),(1600,1999),(2000,2399),(2400,2799),(2800,3199)]
for score in a:
  ind = check(score)
  if ind==-1:
    thopes+=1
  else:
    colors.add(ind)
n = len(colors)
print(max(1,n),thopes+n)