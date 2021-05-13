N,X = [int(IN) for IN in input().split()]
L = [int(l) for l in input().split() ]

D = 0
for i in range(len(L)) :
  D += L[i]
  if D > X:
    print(i+1)
    exit()

print(len(L)+1)