X, Y = map(int, input().split())
for a in range(0, X+1):
  if 2*X - Y/2 == a:
    print("Yes")
    exit()
print("No")