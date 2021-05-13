a, b = map(int, input().split())

for n in range(999):
  if n*(n+1)/2 - a == (n+1)*(n+2)/2 - b:
    print(int(n*(n+1)/2 - a))
