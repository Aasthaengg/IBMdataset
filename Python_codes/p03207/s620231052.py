L=list()
N=int(input())
for i in range(N):
  s=int(input())
  L.append(s)
print(sum(L)-(max(L)//2))