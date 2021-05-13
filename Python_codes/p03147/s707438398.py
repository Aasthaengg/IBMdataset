N = int(input())
h = list(map(int,input().split()))
H = h[:]

base = min(h)
count = 0
already_zero = 0
more = 0

while 1:
  if max(H) == 0:
    break
  else:
    for i in range(N):
      if H[i] == 0 and more == 1:
        count += 1
        more = 0
        if i == N - 1:
          break
      else:
        if H[i] != 0:
          H[i] -= 1
          if more == 0:
            more = 1
      
      if more == 0 and i == N - 1:
        break
      
    else:
      count += 1
      more = 0
      already_zero = 0
      
print(count)