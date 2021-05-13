def main():
  num = list(map(int,input().split()))
  flg=0
  if num[0]>num[1]:
    print(num[0]*2-1)
  elif num[1]>num[0]:
    print(num[1]*2-1)
  else:
    print(num[0]*2)
main()