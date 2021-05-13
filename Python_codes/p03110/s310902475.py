N = int(input())
a = 0

for n in range(N):
  x,u = input().split()
  
  if u=="JPY":
    a+=int(x)
  else:
    a+=380000*float(x)

print(a)