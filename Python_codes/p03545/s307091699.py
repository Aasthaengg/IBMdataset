a, b, c, d = map(int, list(input()))

def calc(n, a, b):
  if n == 0:
    return a + b
  else:
    return a - b

pm = "+-"
for i in range(2):
  num = calc(i, a, b)
  for j in range(2):
    num2 = calc(j, num, c)
    for k in range(2):
      num3 = calc(k, num2, d)
      if num3 == 7:
        ans = str(a) + pm[i] + str(b) + pm[j] + str(c) + pm[k] + str(d) + "=7"
        print(ans)
        exit()