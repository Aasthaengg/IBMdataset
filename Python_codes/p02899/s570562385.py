N = int(input())
A = list(map(int, input().split()))

l = [0]*N
for i,a in enumerate(A):
  l[a-1]=i+1
  
for x in l:
  print(x, end=' ')