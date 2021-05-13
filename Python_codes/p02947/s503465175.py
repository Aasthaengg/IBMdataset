from collections import Counter,defaultdict

N=int(input())
count = defaultdict(int)
for i in range(N):
  s=Counter(list(input()))
  count[str(sorted(s.items()))] += 1

count = list(count.values())
SUM = 0
for c in count:
  if c>1:SUM += c*(c-1)//2
print(SUM)