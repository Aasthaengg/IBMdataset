n, k, q = map(int, input().split())
scores = [k-q for i in range(n)]

for i in range(q):
  scores[int(input())-1] += 1
  
for i in range(len(scores)):
  if scores[i] > 0:
    print("Yes")
  else:
    print("No")