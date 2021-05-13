n, k = list(map(int,input().split()))
w = list()
for _ in range(n):
  w.append(int(input()))

w_sum = sum(w)



def f(p):
  v = 0
  for _ in range(k):
    s = 0
    while s + w[v] <= p:
#      print("add", w[v])
      s += w[v]
      v += 1
      if v == n:
        return v
  return v


def search(a, l, r, f):
  while r - l > 1 :
    m = (l + r) // 2
    v = f(m)
    if  v >= n:
      r = m 
    else:
      l = m
  return r

res = search(n, 0, 10000 * 100000, f)
print(res)


