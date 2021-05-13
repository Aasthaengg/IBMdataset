N = int(input())
a = list(map(int,input().split()))

all = 0

for i in range(N):
  all ^= a[i]
for i in range(N):
  print(all^a[i],end = " ")