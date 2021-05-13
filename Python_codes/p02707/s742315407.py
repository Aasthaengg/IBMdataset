def resolve():
  n = int(input())
  a = list(map(int, input().split()))
  b = [0] * n
  for x in a:
    b[x-1] += 1
  for x in b:
    print(x)
  return

if __name__ == "__main__":
  resolve()
