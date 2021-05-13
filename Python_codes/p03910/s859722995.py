N = int(input())
def floor(x):
  if x == int(x):
    return x
  else:
    return int(x)+1
m = floor(((1+8*N)**0.5 - 1 ) /2)
S = ((m+1)*m) // 2
skip = S - N
for i in range(int(m)):
  if i+1 == skip:
    continue
  print(i+1)