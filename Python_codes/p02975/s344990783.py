N = int(input())
al = list(map(int,input().split()))
bit = [0]*35

for i in range(N):
  for j in range(35):
    if (al[i]>>j)&1 == 1:
      bit[j] += 1
      
for j in range(35):
  if bit[j] %2 == 1:
    print("No")
    exit()
    
print("Yes")