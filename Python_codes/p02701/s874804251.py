N = int(input())
d = dict()
for i in range(N):
  prize = input()
  if not prize in d:
    d[prize] = 1
print(len(d))