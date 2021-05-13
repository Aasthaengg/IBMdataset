import sys
# input = sys.stdin.readline

def main():
  n, k = map(int, input().split())
  alist = list(map(int, input().split()))
  suma = sum(alist)
  i = 1
  yaku = []
  while i*i<=suma:
    if suma % i == 0:
      yaku.append(i)
      if suma//i != i:
        yaku.append(suma//i)
    i += 1

  for d in sorted(yaku, key=lambda x: -x):
    rem = [a%d for a in alist]
    rem = list(sorted(rem))
    sumr = d*len(rem) - sum(rem)
    kc = 0
    for _r in rem:
      kc += _r
      sumr = sumr - (d-_r)
      if max(kc, sumr) <= k:
        print(d)
        sys.exit(0)


if __name__ == '__main__':
  main()
