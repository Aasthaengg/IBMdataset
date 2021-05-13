n, m = map(int, input().split())

stairs = ["o"] * (n + 1)

for _ in range(m):
  stairs[int(input())] = "x"

c = [0] * (n + 1)
c[0] = 1
if stairs[1] == "x":
  c[1] = 0
else:
  c[1] = 1

for i in range(2, n + 1):
  if stairs[i] == "x":
    c[i] = 0
  else:
    c[i] = c[i - 1] + c[i - 2]

print(c[n] % 1000000007)