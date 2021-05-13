n,m = map(int,input().split())
a = list(map(int,input().split()))
bcl = [list(map(int,input().split())) for nesya in range(m)]
bcl.sort(reverse=True,key=lambda x:x[1])
t = 0
for bc in bcl:
  t += bc[0]
  a += [bc[1]]*bc[0]
  if t > n:
    break
a.sort(reverse=True)
print(sum(a[:n]))