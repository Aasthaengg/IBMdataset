N,K=[int(i) for i in input().split(" " )]
s = []
for i  in  range(N):
  s.append([int(ii) for ii in input().split(" ")])

s.sort( key=lambda x: x[0])  
countPush = 0
for i in s:
   countPush += i[1]
   if(countPush >= K ):
     print(i[0])
     break
