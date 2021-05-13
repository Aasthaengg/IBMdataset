n = int(input())
a = list(map(int, input().split()))
b = [a[i] for i in range(n) if i % 2 == 0]
c = [a[i] for i in range(n) if i % 2 == 1]
if n % 2 == 0:
  d = c[::-1] + b
elif n % 2 == 1:
  d = b[::-1] + c
s = ' '.join([str(e) for e in d])
print(s)