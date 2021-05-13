part = set()
S = input()
K = int(input())

part.add(S)
for i in range(len(S)):
  for j in range(i,i+K):
    part.add(S[i:j+1])
    
part = list(part)
part.sort()
print(part[K-1])
