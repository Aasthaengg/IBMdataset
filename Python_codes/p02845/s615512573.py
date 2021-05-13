import itertools

N = int(input())
Ali = list(map(int,input().split()))
C = [0,0,0]

for i in range(N):
  n = 0
  for j in range(3):
    if C[j] == Ali[i]:
      C[j] += 1
      break
  
Ali = Ali[::-1]
if C[0] == C[1] == C[2]:
  r = 1
elif C[0] == C[1] or C[1] == C[2] or C[2] == C[0]:
  r = 3
else:
  r = 6

  
for i in range(N):
  n = 0
  ta = 0 
  for j in range(3):
    if C[j]-1 == Ali[i]:
      n += 1
      ta = j
  r *= n
  C[ta] = Ali[i]
  
print(r%1000000007)