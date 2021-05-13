N=int(input())
A,B=map(int,input().split())
P=list(map(int,input().split()))
count =[0,0,0]

for p in P:
  if p <= A:
    count[0] += 1
  elif A < p and p <= B:
    count[1] += 1
  else:
    count[2] += 1

min = 100    
for i in count:
  if min > i:
    min = i
print(min)
