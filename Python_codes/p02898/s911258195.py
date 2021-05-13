n,k = map(int,input().split())
ans = 0
h = list(map(int,input().split()))
h.sort()
if h[n-1] < k:
    print(0)
    exit()
while True:
  if h[ans] >= k:
    break
  else:
    ans += 1
print(len(h[ans:]))