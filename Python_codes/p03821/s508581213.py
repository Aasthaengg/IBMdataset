from sys import stdin
def main():
  readline = stdin.readline
  N = int(readline())
  L = [list(map(int, readline().split())) for _ in range(N)]
  cnt = 0
  for l in L[::-1]:
    a = l[0]
    if a == 0:
      continue
    a += cnt
    b = l[1]
    if a <= b:
      cnt += b - a
    else:
      cnt += (b - a % b) % b
  print(cnt)
if __name__ == "__main__":
  main()