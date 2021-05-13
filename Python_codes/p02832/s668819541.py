n = int(input())
a = [int(x) for x in input().split()]

tmp = 1
s = set()
for x in a:
  if x == tmp:
    s.add(x)
    tmp += 1

print(n - len(s) if s else -1)