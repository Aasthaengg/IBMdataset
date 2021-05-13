N,X = (int(x) for x in input().split())
L = [int(x) for x in input().split()]
s = 0
i = 0
while (s <= X):
  if i >= N:
    print(N+1)
    quit()
  else:
    s = s + L[i]
    i = i + 1
print(i)