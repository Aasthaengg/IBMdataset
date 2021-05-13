
def main():
  n, k = map(int, input().split())

  mod = 10 ** 9 + 7

  if n == k:
    ans = 1
    for num in input().split():
      ans = (ans * int(num)) % mod

    print(ans % mod)
    return

  plus = []
  minus = []
  for num in input().split():
    num = int(num)
    if num >= 0:
      plus.append(num)
    else:
      minus.append(num)

  pn = len(plus)
  mn = len(minus)

  if pn == 0 and k % 2 == 1:
    minus.sort(reverse = True)
    ans = 1
    for i in range(k):
      ans = (-ans * minus[i]) % mod

    print((-ans) % mod)
    return


  plus.sort(reverse = True)
  minus.sort()

  pi = 0
  mi = 0

  while k > 0:
    if pi + 1 == pn:
      if k % 2 == 0:
        mi += k
      else:
        pi += 1
        mi += k - 1

      break

    if pi == pn:
      mi += k
      break

    if mi + 1 >= mn:
      pi += k
      break

    if k == 1 or plus[pi] * plus[pi + 1] >= minus[mi] * minus[mi + 1]:
      pi += 1
      k -= 1
    else:
      mi += 2
      k -= 2

  ans = 1
  for i in range(pi):
    ans = (ans * plus[i]) % mod

  for i in range(mi):
    ans = (-ans * minus[i]) % mod

  print(ans % mod)


main()
