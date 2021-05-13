N=int(input())
L=list(map(int,input().split()))
L.sort()
L=L[::-1]
R=0
for i in range(N):
  R=R+L[2*i+1]
print(R)