n = input()
k = len(n)
a = 9 * (k - 1) + int(n[0]) - 1
b = 0
for i in range(k):
  b += int(n[i])
c = 0
m = ''
if k > 2 and n[-2] != '0':
  m = str(int(n))[:k - 2] + str(int(n[-2]) - 1) + '9'
elif k > 2 and n[-2] == '0':
  m = str(int(n) - (int(n[-1]) + 1))
for i in range(len(m)):
  c += int(m[i])
ans = max(a, b, c)
print(ans)