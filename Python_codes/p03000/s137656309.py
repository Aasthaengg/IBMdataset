N, X = map(int, input().split())
L = list(map(int, input().split()))
z = 0
L.insert(0,0)
for i in range(len(L)):
  bound = i+1
  z += L[i]
  if z > X:
    bound -= 1
    break
print(bound)