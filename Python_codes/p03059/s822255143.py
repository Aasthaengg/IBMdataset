A,B,T = map(int,input().split())
time = 0
bis = 0
while (time + A <= T+0.5):
  bis += B
  time += A
print(bis)
  
  
