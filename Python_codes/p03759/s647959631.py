def main():
  num = list(map(int,input().split()))
  if num[1]*2==num[0]+num[2]:
    print('YES')
  else:
      print('NO')
main()