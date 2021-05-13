n=int(input())
lo=2
li=1
cou=0
import sys
if n==1:
    print(1)
    sys.exit()
if n==2:
    print(3)
    sys.exit()

for  i in range(n-1):

    cou=lo+li
    lo=li
    li=cou
   

print(cou)



