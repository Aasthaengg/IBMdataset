N = int(input())

sup = int(N // 2) + 1

L = []

for i in range(1,sup):
  diff = N - i
  pair = [i,diff]
  pair = set(pair)
  if len(pair) == 2:
    L.append(pair)


    
print(len(L))
