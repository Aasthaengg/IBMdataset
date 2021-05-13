n = int(input())
abc = [list(map(int, input().split())) for _ in range(n)]

a, b, c = [0], [0], [0]
for i in abc:
  aa = i[0] + max(b[-1], c[-1])
  bb = i[1] + max(c[-1], a[-1])
  cc = i[2] + max(a[-1], b[-1])
  a.append(aa)
  b.append(bb)
  c.append(cc)
print(max(a[-1], b[-1], c[-1]))