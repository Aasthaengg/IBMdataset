N,x = input().split()
A = input().split()
a = []
for i in range(int(N)):
  a.append(int(A[i]))
  
a.sort()
X = int(x)
 
idx = 0
while X>0 and idx<int(N):
  X = X-a[idx]
  idx+=1

if X==0:
  idx+=1
  
print(idx-1)