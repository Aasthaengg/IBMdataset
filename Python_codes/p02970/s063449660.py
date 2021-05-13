n,d = map(int,input().split())
a = 1
while (2*d+1)*a < n:
  a += 1
print(a)