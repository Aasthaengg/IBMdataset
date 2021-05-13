d = {"DUMMY": 0}
n = int(input())
for i in range(n):
  s = input()
  d[s] = d.get(s, 0) + 1

n = int(input())
for i in range(n):
  s = input()
  d[s] = d.get(s, 0) - 1

print(max(d.values()))