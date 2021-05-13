n = int(input())
v = list(map(int,input().split()))
c = list(map(int,input().split()))

x = [0]
for i in range(n):
  if (v[i] - c[i]) >= 0:
    x.append(v[i] - c[i])
  
print(sum(x))
