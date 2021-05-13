n = int(input())
a, b = map(int, input().split())
l = [int(x) for x in input().split()]

aa, ab, bb = [], [], []

for x in l:
  if x <= a:
    aa.append(x)
  elif a + 1 <= x and x <= b:
    ab.append(x)
  else:
    bb.append(x)

print(min(map(len, [aa, ab, bb])))