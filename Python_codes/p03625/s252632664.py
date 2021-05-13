n = int(input())
a = sorted(list(map(int, input().split())), reverse=True) + [0, 0, 0, 0]
l = []
for i in range(len(a) - 1):
  if a[i] == a[i + 1] and (len(l) == 0 or l[-1] != i - 1):
    l.append(i)
    if len(l) >= 2:
      break
print(a[l[0]] * a[l[1]])
