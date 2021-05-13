n, m, x = list(map(int, input().split()))

a = [0] * (n + 1)
c = list(map(int, input().split()))
for v in c:
  a[v] = 1
print(min(sum(a[0:x]), sum(a[x:n+1])))