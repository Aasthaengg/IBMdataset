n,k = map(int,input().split())

B = input()
happy = 0
for i in range(n):
  if B[i]=="L" and i != 0 :
    if B[i-1] == "L":
      happy +=1
  if B[i]=="R" and i != n-1 :
    if B[i+1] == "R":
      happy +=1
print(min(happy+2*k, n-1))
