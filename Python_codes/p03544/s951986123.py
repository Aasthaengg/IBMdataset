n = int(input())

L = [2,1]
for i in range(2,n+1):
  k = L[i-2]+L[i-1]
  L.append(k)
  
print(L[len(L)-1])
