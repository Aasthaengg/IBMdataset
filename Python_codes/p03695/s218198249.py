N = int(input())
A = list(map(int,input().split()))
C = []
D = 0
ans = []

for a in A:
  if a<3200:
    C+=[a//400]
  else:
    D+=1

if D==0:
  ans = [len(set(C)),len(set(C))]
else:
  if len(C)==0:
    ans = [1,D]
  else:
    ans = [len(set(C)),len(set(C))+D]

print(*ans)