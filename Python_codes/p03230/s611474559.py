import sys
N=int(input())

for k in range(1,10**9):
  if N==k*(k+1)//2:
    break
  elif N<k*(k+1)//2:
    print("No")
    sys.exit(0)
  
print("Yes")
print(k+1)

cnt=1
set_list=[set() for _ in range(k+1)]
for i in range(k+1):
  for j in range(i+1,k+1):
    #print(i,j)
    set_list[i].add(cnt)
    set_list[j].add(cnt)
    cnt+=1
#print(set_list)
  
for i in range(k+1):
  print(k,*set_list[i])