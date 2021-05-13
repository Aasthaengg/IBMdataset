h, w, a, b = map(int, input().split())
s = [[1 for _ in range(a)] + [0 for _ in range(w-a)] for _ in range(b)]
for _ in range(h-b):
  s.append([0 for i in range(a)] + [1 for i in range(w-a)])
for i in range(h):
  print(''.join(list(map(str, s[i]))))