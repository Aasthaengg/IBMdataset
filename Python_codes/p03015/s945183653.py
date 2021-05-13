MOD = 10 ** 9 + 7


def main():
  L = input().strip()
  l = len(L)
  assert l > 0

  dp1 = [-1] * l
  dp2 = [-1] * l
  dp1[0] = 1
  dp2[0] = 2
  for k in range(1, l):
    dp1[k] = dp1[k - 1] * 3 % MOD

    if L[k] == '1':
      dp1[k] += dp2[k - 1]
      dp2[k] = dp2[k - 1] * 2 % MOD
    else:
      dp2[k] = dp2[k - 1]

  return (dp1[-1] + dp2[-1]) % MOD


if __name__ == '__main__':
  print(main())