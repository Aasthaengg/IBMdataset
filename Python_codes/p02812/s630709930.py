n = int(input())
s = input()

iter = 0
for i in range(n):
  res = s[i:i+3]
  if res == "ABC":
    iter += 1

print(iter)