x, n = map(int,input().split())
lst = list(map(int,input().split()))
i = 0
while True:
  if ((x - i) not in lst):
    print(x - i)
    break
  if ((x + i) not in lst):
    print(x + i)
    break
  i = i + 1