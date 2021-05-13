from collections import Counter
N = int(input())
A = [int(x) for x in input().split()]
pair = []
c = Counter(A)
for x,cnt in c.items():
  pair += [x]*(cnt//2)

pair.sort()

answer = 0
if len(pair)>= 2:
  answer = pair[-1] * pair[-2]

print(answer)
