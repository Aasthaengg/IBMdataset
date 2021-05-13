N,P=list(map(int,input().split()))
l= list(map(int,input().split()))
l=[i%2 for i in l]
if sum(l) == 0:
   print((P==0)*2**N)
else:
   print(2**(N-1))