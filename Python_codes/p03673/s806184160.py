n = int(input())
a = list(map(int, input().split()))
b1 = []
b2 = []
m = n % 2
for i in range(n):
  if i % 2 == m:
    b1.append(a[i])
  else:
    b2.append(a[i])
b2 = b2[::-1]
b = b2 + b1
b = [str(bb) for bb in b]
b = ' '.join(b)
print(b)