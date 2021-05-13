from collections import defaultdict

N=int(input())
count = defaultdict(int)
for i in range(N):
  s = input()
  s = ''.join(sorted(s))
  count[s] += 1

SUM = 0
for val in count.values():
  if val > 1:SUM+=val*(val-1)//2
print(SUM)