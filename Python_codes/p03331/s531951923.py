def calc(a):
  ret = 0
  while a != 0:
    ret += a % 10
    a //= 10
  return ret

def resolve():
  n = int(input())
  ans = 1000000000
  for a in range(1, n):
    b = n - a
    ans = min(ans, calc(a) + calc(b))
  print(ans)
  return

if __name__ == "__main__":
  resolve()
