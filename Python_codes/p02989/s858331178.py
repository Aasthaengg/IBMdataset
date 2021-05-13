n=int(input())
d=list(map(int,input().split()))

d.sort()

a=d[n//2]
b=d[n//2-1]

if a==b:
  print('0')

else:
  print(a-b)