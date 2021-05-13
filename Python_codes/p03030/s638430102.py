n = int(input())
d = list(list(input().split())+[i+1] for i in range(n))
a = sorted(d, key=lambda x:(x[0],-int(x[1])))
for v in a:
  print(v[2])