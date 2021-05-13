from sys import stdin
input = stdin.readline


def main():
  N, M = list(map(int, input().split()))
  PS = []
  for i in range(M):
    p, s = input().split()
    PS.append((int(p)-1, s))

  penas = [0]*(N)
  is_ac = [0]*(N)
  for i in range(M):
    p, s = PS[i]
    if s == 'AC':
      is_ac[p] = True
    elif not is_ac[p]:
      penas[p] += 1

  num_ac = sum(is_ac)
  num_pe = 0

  for i in range(N):
    if is_ac[i]:
      num_pe += penas[i]

  print(num_ac, num_pe)


if(__name__ == '__main__'):
  main()
