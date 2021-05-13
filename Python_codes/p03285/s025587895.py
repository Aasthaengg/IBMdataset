n = int(input())

l = [0] * 10000
for i in range(0, 100 + 1):
  for j in range(0, 100 + 1):
    # print(f"{i} {j}")
    val = (4 * i) + (7 * j)
    # l.append(val)
    l[val] += 1
# print(max(l))

if l[n] == 0:
    print('No')
else:
    print('Yes')