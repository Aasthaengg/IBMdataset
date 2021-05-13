N,D=map(int,input().split())
#print (N,D)
number=N//(2*D+1)
amari=N%(2*D+1)
#print(number, amari)
if amari != 0:
  number=number+1
print(number)