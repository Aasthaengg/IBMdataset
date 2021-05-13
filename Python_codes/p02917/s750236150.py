n = int(input())
b = list(map(int, input().split()))
ar = [b[0]]

for i in range(n-2):
  if b[i] <= b[i+1]:
    
    ar.append(b[i])
  else:
    
    ar.append(b[i+1])
ar.append(b[-1])
print(sum(ar))