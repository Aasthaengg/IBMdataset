k = int(input())
n = 50
p,q = k//n,k%n
l = list(range(p-q,50+p-q))
for i in range(q):
  l[i] += n+1
print(n)
print(" ".join(map(str,l)))