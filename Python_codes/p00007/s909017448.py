#Volume0-0007
a = int(input())
n = int(100000)
for w in range(a):
  if (n*1.05)%1000 == 0:
    n = n*1.05
  else:
    n = n*1.05//1000*1000+1000
print(int(n))
