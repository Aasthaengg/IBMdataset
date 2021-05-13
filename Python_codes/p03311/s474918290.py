n = int(input())
a = list(map(int, input().split()))


def sadness(b):
  sad = 0
  for i, e in enumerate(a):
    i += 1
    sad += abs(e - (b + i))
  return sad


d = []
for i, e in enumerate(a):
  i += 1
  d.append(e - i)

d.sort()

if len(d) % 2 == 1:
  print(sadness(d[len(d) // 2]))
else:
  print(min(sadness(d[len(d) // 2]), sadness(d[len(d) // 2 + 1])))
