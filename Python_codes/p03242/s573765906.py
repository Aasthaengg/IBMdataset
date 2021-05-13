n=input()
N=0
for i in range(3):
  if n[i]=="1" :
    N+=9
  else :
    N+=1
  N*=10
print(N//10)