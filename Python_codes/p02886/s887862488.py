def k(n):
  return n**2
a=int(input())
L=list(map(int,input().split()))
c=sum(L)
c=c**2
L=list(map(k,L))
d=sum(L)
print((c-d)//2)