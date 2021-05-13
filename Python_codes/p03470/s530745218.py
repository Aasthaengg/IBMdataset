N = int(input())
h = []
for i in range(N):
  m = input()
  if h.count(m) == 0:
    h.append(m)
print(len(h))