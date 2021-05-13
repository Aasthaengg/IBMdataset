N=int(input())
V=list(map(int, input().split()))
V.sort()
tmp=(V[0]+V[1])/2
for i in range(2,N):
  tmp=(tmp+V[i])/2
print(tmp)