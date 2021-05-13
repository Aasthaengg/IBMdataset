def main():
  num = list(map(str,input().split()))
  if num[0][-1]==num[1][0] and num[1][-1]==num[2][0]:
    print('YES')
  else:
    print('NO')
main()