X, Y = map(int, input().split())

for i in range(X + 1):
  tsuru = X - i
  leg = 4 * i + 2 * tsuru
  
  if Y == leg:
    print("Yes")
    exit()

print("No")