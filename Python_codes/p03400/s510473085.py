N = int(input())
D,X = map(int, input().split())

A =[]
for i in range(N):
  A +=[int(input())]

ate=0
for j in range(D):
  for a in A:
    if j%a==0 :
      ate+=1
      
print(X + ate)