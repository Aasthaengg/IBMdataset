N, K = map(int, input().split())
array = [0]*(10**5+ 1)

for i in range(N):
  a, b = map(int, input().split())
  array[a]+= b
  
S = 0
i = 0

while S < K:
  S+= array[i]
  i+= 1
  
print(i- 1)