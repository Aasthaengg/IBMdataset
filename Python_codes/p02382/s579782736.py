n = int(input())
x = list(map(int, input().split())) 
y = list(map(int, input().split()))
c = [abs(x[i]-y[i]) for i in range(n)]
for p in range(1, 4):
  ans = 0
  for s in c:
    ans += s**p
  print("{:.6f}".format(ans**(1/p)))
print("{:.6f}".format(max(c)))
