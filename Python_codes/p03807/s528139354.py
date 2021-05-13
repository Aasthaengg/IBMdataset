def main():
  ans = 'YES'
  n = int(input())
  l = list(map(int, input().split()))
  if sum(l)%2 != 0:
      ans = 'NO'
  print(ans)

if __name__ == '__main__':
  main()