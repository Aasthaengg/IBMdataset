def gcd(a, b, c):
  x = gcd2(a, b)
  y = gcd2(b, c)
  return gcd2(x, y)

def gcd2(x, y):
    if y == 0:
        return x
    else:
        return gcd2(y,x%y)

def main():
  K = int(input())
  ans = 0
  for p in range(1, K+1):
    for s in range(p, K+1):
      for k in range(s, K+1):
        if p == s == k:
          ans += p
        elif p == s or s == k or p == k:
          ans += 3 * gcd(p, s, k)
        else:
          ans += 6 * gcd(p, s, k)
  print(ans)

if __name__=='__main__':
    main()