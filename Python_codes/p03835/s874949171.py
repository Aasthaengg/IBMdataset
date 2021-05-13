MM = input().split()
K = int(MM[0])
S = int(MM[1])
count = 0
for a in range(K+1):
  for b in range(K+1):
    z = S-a-b
    if 0<= z <=K:
      count +=1
print(count)