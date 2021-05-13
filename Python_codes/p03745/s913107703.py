N = int(input())
A = list(map(int, input().split(" ")))

list = []
sim=0
for i in range(N-1):
  if A[i]<A[i+1]:
    list.append(1)
  if A[i]>A[i+1]:
    list.append(0)
  if A[i]==A[i+1]:
    sim+=1
    
i = 0
count = 0

while i<N-2-sim:
  if list[i] != list[i+1]:
    count += 1
    i+=1
  i+=1

print(count + 1)