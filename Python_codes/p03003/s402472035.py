M = int(1e+9 + 7)


def main():
  input()
  s = list(map(int, input().split()))
  t = list(map(int, input().split()))
  z = [0] * len(t)

  for v in s:
    c = 0

    for i, w in enumerate(t):
      y = z[i]

      if v == w:
        z[i] = (z[i] + c + 1) % M

      c = (c + y) % M

  y = 0

  for v in z:
    y = (y + v) % M

  y = (y + 1) % M

  print(y)


if __name__ == '__main__':
  main()
