def cor(m):
  if m % 2 == 0:
    return m//2 
  else:
    return 3*m + 1

n = int(input())
arr = [n]
for i in range(10**6):
  nn = cor(n)
  if nn in arr:
    print(i+2)
    exit()
  else:
    arr.append(nn)
    n = nn
