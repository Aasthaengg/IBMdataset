H1,M1,H2,M2,K = map(int,input().split())
start = H1*60 + M1
finish = H2*60 + M2 - K

if finish - start >= 0:
  print(finish - start)
else:
  print(0)