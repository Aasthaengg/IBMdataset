N=int(input())
total = 0
for i in range(N):
  x,u=input().split()
  total = total + float(x) * [1,380000.0][u=="BTC"]
print(total)