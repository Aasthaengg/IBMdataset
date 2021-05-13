n = int(input())
ab = sorted([list(map(int, input().split())) for _ in range(n)], key = lambda i: i[1])

t = 0
for i in ab:
  t += i[0]
  if t > i[1]:
    print("No")
    exit()
print("Yes")