N = int(input())
L = list(map(int, input().split()))
s = []
c = 0
for i in range(1, len(L)):
  if L[i-1] < L[i]:
    s.append(c)
    c = 0
  else:
    c += 1
s.append(c)
print(max(s))
