x = 0
N = int(input())
S = input()
L = [x]
for t in S:
  if t == 'I':
    x += 1
    L.append(x)
  else:
    x -= 1
    L.append(x)
print(max(L))