A,B=map(int,input().split())
res = 1
RES = 0
while res < B:
  res = res - 1 + A
  RES += 1
print(RES)