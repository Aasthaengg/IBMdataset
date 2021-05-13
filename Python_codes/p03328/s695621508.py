A,B = map(int,input().split())

Ha = (B-A-1)*(B-A)//2

for x in range(1,Ha):
  if Ha-x == A:
    print(x)
    exit()