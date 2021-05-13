N,A,B=list(map(int,input().split()))
if A == B:
   print(1)
   exit()
if N ==1 or A>B:
   print(0)
   exit()
ans=(N-2)*(B-A)
print(ans+1)
