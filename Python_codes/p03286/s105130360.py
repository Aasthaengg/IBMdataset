N=int(input())
ans=""
for i in range(1,10000):
   tmp=2**i
   if N%tmp==2**(i-1):
      N-=(-2)**(i-1)
      ans="1"+ans
   else:
      ans="0"+ans
   if N == 0:
      break
print(ans)