n = int(input())
a = list(map(int, input().split()))
b = [bin(i)[2:] for i in a]
c = [0] * n
for i,v in enumerate(b):
  for j in v[::-1]:
    if j == '0':
      c[i] += 1
    else:
      break
print(min(c))