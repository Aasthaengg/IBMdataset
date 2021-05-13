def main():
  ans = 'YES'
  n = int(input())
  l = list(map(int, input().split()))
  a = 0
  for i in l:
      if i % 2 != 0:
          a += 1
  if a % 2 != 0:
      ans = 'NO'
  print(ans)

if __name__ == '__main__':
  main()