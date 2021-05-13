N = int(input())
ctr = 0
for i in range (1, N+1):
  if (i>0 and i<10) or (i>99 and i<1000) or (i>9999 and i<100000):
    ctr += 1
print(ctr)