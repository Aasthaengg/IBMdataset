N=int(input())
p=sorted([int(input()) for i in range(N)])[::-1]

Sum=p[0]/2

for i in range(1,N):
  Sum=Sum+p[i]

print(int(Sum))