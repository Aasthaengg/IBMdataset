import bisect
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
ad=sorted(a)
bd=sorted(b)
cd=sorted(c)
#print(ad)
#print(bd)
#print(cd)
count=0
for i in range(n):
  al=bisect.bisect_left(ad,bd[i])
  cl=bisect.bisect_right(cd,bd[i])
  sum=al * ( n - cl )
  #print(str(al) + " " + str(cl) + " " + str(sum))
  count=count+( al * ( n - cl ) )
print(count)