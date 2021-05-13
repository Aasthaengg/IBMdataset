N, X = list(map(lambda a: int(a), input().split(" ")))
L = list(map(lambda b: int(b), input().split(" ")))

i = 0
s = 0
while(s <= X and i < len(L)):
  s += L[i]
  i += 1

if s <= X:
  i += 1

print(i)