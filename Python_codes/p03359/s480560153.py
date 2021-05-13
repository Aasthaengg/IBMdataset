a, b = map(lambda x: int(x), input().split())

num = a-1

if b >= a:
  num += 1

print(num)