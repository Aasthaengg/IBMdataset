n = int(input())
#d = {"JPY":0,"BTC":0}
x = 0
for i in range(n):
  a,u = input().split()
  a = float(a)
  if u=="JPY":
    x += a
  elif u=="BTC":
    x += (a*380000.0)
print(x)