import bisect


def main():
  D, G = list(map(int, input().split()))
  P = []
  for i in range(1, D+1):
    P.append(tuple(map(int, input().split())))

  # print(D, G, P)
  minp = float('inf')
  for bit in range(1 << D):
    total = 0
    num_p = 0
    bset = set()
    for i in range(D):
      mask = 1 << i
      if bit & mask:
        total += P[i][1] + 100*(i+1)*P[i][0]
        num_p += P[i][0]
        bset.add(i)

    # print(f'bset:{bset}, num_p:{num_p}')

    res = G - total
    if res <= 0:
      if num_p < minp:
        minp = num_p
      continue

    for i in reversed(sorted(set([i for i in range(D)]) - bset)):
      maxv = 100*(i+1) * (P[i][0]-1)

      if res <= maxv:
        num_take = max(min(bisect.bisect(list(range(0, maxv+100*(i+1), 100*(i+1))), res)-1, P[i][0]-1), 1)
        # print(i, list(range(0, maxv, 100*(i+1))))
        # print(f'res:{res} so solve {100*(i+1)} * {num_take}')
        num_p += num_take
        res -= 100*(i+1)*num_take
        if num_p < minp:
          minp = num_p
        break

      res -= maxv
      # print(f'solve {i+1} * {P[i][0]-1}')
      num_p += (P[i][0]-1)

  print(minp)


if(__name__ == '__main__'):
  main()