a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = [list(map(int, input().split())) for i in range(a[2])]
e = [min(b) + min(c)]
for f in d:
  e.append(b[f[0] - 1] + c[f[1] - 1] - f[2])
print(min(e))  
