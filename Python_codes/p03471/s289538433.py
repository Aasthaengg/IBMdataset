from sys import stdin
n,y = [int(x) for x in stdin.readline().rstrip().split()]
flag = False

for p in reversed(range(n+1)):
   if p * 10000 > y:
      continue
   else:
      for q in reversed(range(n-p+1)):
         if 10000*p + 5000*q + 1000*(n-p-q) == y:
            print(p,q,n-p-q)
            flag = True
            break
      if flag == True:
         break
   if flag == True:
      break
if flag == False:
   print(-1,-1,-1)