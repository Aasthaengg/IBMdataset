from collections import defaultdict, Counter

def main():
  H, W, N, *A = map(int,open(0).read().split())
  D = defaultdict(int)

  while A:
    b, a = A.pop(), A.pop()
    for i in [a - 2, a - 1, a]:
      if 1 <= i <= H - 2:
        for j in [b - 2, b - 1, b]:
          if 1 <= j <= W - 2:
            D[(i, j)] += 1

  print((H - 2) * (W - 2) - len(D))

  c = Counter(D.values())
  for i in range(1, 10):
    print(c.get(i, 0))

if __name__ == '__main__':
  main()