def main():
  num = list(map(int,input().split()))
  if (num[0] + num[1])>= 10:
    print('error')
  else:
    print(num[0]+num[1])
      
main()