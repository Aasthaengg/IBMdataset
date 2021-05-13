N=int(input())
def calc(n):
  return n*(n+1)//2

threshold=0
for i in range(1,N+1):
  if calc(i)>=N:
    threshold=i
    break

sub=calc(threshold)-N
#print(sub)
for a in range(1,threshold+1):
  if a!=sub:
    print(a)