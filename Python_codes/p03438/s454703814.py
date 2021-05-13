n = int(input())
c = 0
for i,j in zip(map(int,input().split()),map(int,input().split())):
  if i > j:
    c -= i-j
  else:
    c += (j-i)//2
print('YNeos'[c<0::2])