N = int(input())
ans = 0

for i in range(0,N):
  x, u = map(str,input().split())
  x = float(x)
  if u == "JPY":
    ans = ans+x
  elif u == "BTC":
    ans = ans+380000.0*x
    
print(ans)