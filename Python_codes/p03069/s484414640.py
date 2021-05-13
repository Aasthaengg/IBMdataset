
import bisect

N = int(input())
S = '0'+input()+'0'

lst1 = []
lst2 = [0]*(N+2)


for i in range(1,N+1):
  if S[i] == '#':
    lst1.append(i)
  if S[N+1-i] == '.':
    lst2[N+1-i] = lst2[N+2-i] + 1
  else:
    lst2[N+1-i] = lst2[N+2-i]
    

if len(lst1) == N or lst2[1] == N:
  print(0)
  exit()
  
rlt = N+1
for i in range(len(lst1)):
  rlt =  min(rlt, i+lst2[lst1[i]])
  
rlt = min(len(lst1), rlt)
  
print(rlt)