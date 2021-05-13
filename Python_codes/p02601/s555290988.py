a, b, c = map(int, input().split())
k = int(input())

if b > a:
  multiplier = 2 ** k
  if c * multiplier > b:
    ans = 'Yes'
  else:
    ans = 'No'
else:
  while b <= a:
    b *= 2
    k -= 1
  multiplier = 2 ** k
  if c * multiplier > b:
    ans = 'Yes'
  else:
    ans = 'No'

print(ans)
