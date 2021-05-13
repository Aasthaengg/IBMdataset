N = int(input())
vs = list(map(int,input().split()))
vs.sort()
c = vs[0]
for i in range(1,N):
  c = (c + vs[i])/2
print(c)