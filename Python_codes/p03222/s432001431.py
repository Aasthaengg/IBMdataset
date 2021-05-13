#16:10
h,w,k = map(int,input().split())
mod = 10 ** 9 + 7
fib = [1,1,2,3,5,8,13,21,34]
now = [1] + [0] * w
if w > 1:
  for _ in range(h):
    last = now
    now = [0 for _ in range(w)]
    for i in range(w):
      if i == 0:
        now[i] += last[i] * fib[w-1] % mod
        now[i+1] += last[i] * fib[w-2] % mod
      elif i == w-1:
        now[i] += last[i] * fib[w-1] % mod
        now[i-1] += last[i] * fib[w-2] % mod
      else:
        now[i] += last[i] * fib[i] * fib[w-1-i] % mod
        now[i-1] += last[i] * fib[i-1] * fib[w-1-i] % mod
        now[i+1] += last[i] * fib[i] * fib[w-2-i] % mod
  print(now[k-1] % mod)
else:
  print(1)