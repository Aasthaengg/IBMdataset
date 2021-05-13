N=int(input())
p=[0]*N
for i in range(N):
  p[i]=int(input())
print(sum(p)-max(p)//2)