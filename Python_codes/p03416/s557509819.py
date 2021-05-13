A=[int(x) for x in input().split()]
lower=A[0]//100
upper=A[1]//100
count=upper-lower+1
if A[0]>lower*100+int(str(lower)[0])+int(str(lower)[1])*10:
  count-=1
if A[1]<upper*100+int(str(upper)[0])+int(str(upper)[1])*10:
  count-=1
print(count)