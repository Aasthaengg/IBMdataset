n = int(input())
s = input()
r = []
g = []
b = [0]*40000
for i,j in enumerate(s):
  if j == 'R':
    r.append(i)
  if j == 'G':
    g.append(i)
  if j == 'B':
    b[i] += 1
cnt = len(r)*len(g)*sum(b)
for i in r:
  for j in g:
    if b[2*j-i] == 1 :
      cnt -= 1
    if b[2*i-j] == 1 :
      cnt -= 1
    if (i+j)%2 == 0 and b[(i+j)//2] == 1:
      cnt -= 1
print(cnt)