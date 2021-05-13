W,B = map(int, input().strip().split(' '))

ans = []
width = 100

# 上半分
if B == 1:
  ans.append('.'*width)
b = 1
while b < B:
  line = ['.']*width
  for i in range(0,width,2):
    if b >= B: break
    b += 1
    line[i] = '#'
  ans.append(line)
  ans.append('.'*width)

#下半分
if W == 1:
  ans.append('#'*width)
w = 1
while w < W:
  line = ['#']*width
  for i in range(0,width,2):
    if w >= W: break
    w += 1
    line[i] = '.'
  ans.append('#'*width)
  ans.append(line)

print(len(ans), width)
for b in ans:
  print(*b, sep='')

