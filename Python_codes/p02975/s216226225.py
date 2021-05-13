N=int(input())

l=sorted(list(map(int,input().split())))
zero=l.count(0)
if zero==N:
   print("Yes")
   exit()
elif len(set(l)) == 2:
   s=l.count(l[-1])
   if zero==N//3 and s==N*2//3:
      print("Yes")
      exit()
elif len(set(l))==3:
   a,b,c=list(set(l))
   if a^b^c==0 and l.count(a)== l.count(b)==l.count(c):
      print("Yes")
      exit()
print("No")