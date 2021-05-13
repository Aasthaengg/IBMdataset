n, m = map(int, input().split())
an = []

for i in range(n):
  l = [int(num) for num in input().split()]
  an.append(l[1:])

check = {}
for i in an:
  for j in i:
    if j not in check:
      check[j] = 1
    else :
      check[j] += 1

answer = 0
for v in check.values() :
  if v == n:
    answer +=1
      
print(answer)