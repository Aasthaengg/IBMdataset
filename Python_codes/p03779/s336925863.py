x = int(input())
s = 0
j = 0
for i in range(1,x+1):
  s += i
  j += 1
  if s >= x:
    print(j)
    break
