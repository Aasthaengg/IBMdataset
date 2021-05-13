def main():
  n = int(input())
  a = [[]]*n
  for i in range(n):
    a[i] = list(map(int, input().split()))

  a.sort()
  print(a[-1][0]+a[-1][1])

main()