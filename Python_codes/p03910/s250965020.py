N = int(input())

lst = []
i = 1
sm = 0
while sm < N:
  lst.append(i)
  sm += i
  i += 1
  
if sm == N:
  for l in lst:
    print(l)
else:
  a = sm - N
  lst.remove(a)
  for l in lst:
    print(l)