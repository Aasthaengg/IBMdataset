n = int(input())
a = list(map(int, input().split()))


def sadness(b):
  sad = 0
  for i, e in enumerate(a):
    i += 1
    sad += abs(e - (b + i))
  return sad


left, right = -10**9, 10**9 + 1
while right - left > 1:
  mid = (left + right) // 2

  if sadness(mid) > sadness(mid + 1):
    left = mid
  else:
    right = mid

# for b in range(-20, 20):
#   print(b,sadness(b))

print(min(sadness(left), sadness(right)))
