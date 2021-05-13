n, x = map(int, input().split())
L = list(map(int, input().split()))

reach = 0
for i, v in enumerate(L):
  reach += v
  if reach > x:
    print(i + 1)
    exit()
print(n + 1)