r,c = map(int, input().split())
L=[]
for i in range(r):
 al = input()
 print(al, end="")
 AL = list(map(int, al.split()))
 S = sum(AL)
 print(" " + str(S))
 AL. append(S)
 L.append(AL)

for i in range(c):
 S = 0
 for j in range(r):
  S += L[j][i]
 print(str(S) + " ", end="")

S = 0
for j in range(r):
 S += L[j][-1]
print(str(S))