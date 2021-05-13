def hiku(k):
  return abs(k-c)
N=int(input())
L=list(map(int,input().split()))
c=sum(L)/len(L)
L=list(map(hiku,L))
t=min(L)
print(L.index(t))