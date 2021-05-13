n = int(input())
an = list(map(int, input().split()))

r = 1
xor = an[0]
sums = an[0]

cnt = 0
for l in range(n):
  while xor == sums:
    if r >= n:
      r = n + 1
      break
    xor ^= an[r]
    sums += an[r]
    r += 1
    
  cnt += ((r-1) - l)
  xor ^= an[l]
  sums -= an[l]

print(cnt)