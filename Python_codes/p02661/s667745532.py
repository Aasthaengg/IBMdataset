n=int(input())

a=[]
b=[]

for i in range(n):
   x,y=map(int,input().split())
   a.append(x)
   b.append(y)

import statistics as st

am = st.median(a)
bm = st.median(b)

if n % 2 == 1:
   print(int(bm-am+1))
else:
   print(int((bm-am)*2+1))