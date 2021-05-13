A,B,C = sorted(map(int,input().split()))
D = 2*C-A-B

if D%2==0:
  print(D//2)
else:
  print((D+3)//2)