n = int(input())
s = input()
t = input()
x = 2 * n
for i in range(n):
  if t.startswith(s[i:]):
    x = n + i
    print(x)
    exit()
print(x)