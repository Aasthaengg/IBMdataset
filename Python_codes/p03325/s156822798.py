def calc(x):
  ans = 0
  while (x % 2 == 0):
    ans += 1
    x //= 2
  return ans

def resolve():
  n = int(input())
  a = list(map(int, input().split()))
  ans = 0
  for x in a:
    ans += calc(x)
  print(ans)
  return

if __name__ == "__main__":
  resolve()
