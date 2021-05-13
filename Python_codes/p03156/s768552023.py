N = int(input())
A,B = map(int,input().split())
NNN = map(int,input().split())
NN= list(NNN)
counta = 0
countb = 0
countc = 0
for i in NN:
  if i <= A:
    counta += 1
for i in NN:
  
  if A < i <= B:
    countb += 1
for i in NN:
  if B < i:
    countc += 1


print(min(counta,countb,countc))