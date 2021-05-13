K,S = map(int,input().split())
C = 0

for x in range(K+1):
  for y in range(K+1):
    if K>=S-x-y>=0:
      C+=1
        
print(C)