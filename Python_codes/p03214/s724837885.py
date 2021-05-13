def resolve():
  n = int(input())
  a = list(map(int, input().split()))
  avr = sum(a) / n
  b = []
  m = 100000
  for x in a:
    b.append(abs(x - avr))
    m = min(m, abs(x - avr))
  for i in range(len(b)):
    if b[i] == m:
      print(i)
      return
  return

if __name__ == "__main__":
  resolve()
