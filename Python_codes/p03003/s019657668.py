#15:35
h,w = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
mod = 10 ** 9 + 7
now = [1 for _ in range(w+1)]
for i in range(h):
  last = now
  now = [1]
  for j in range(w):
    if a[i] == b[j]:
      now.append((last[j+1]+now[-1])%mod)
    else:
      now.append((last[j+1]+now[-1]-last[j])%mod)
  #print(now)
print(now[-1])