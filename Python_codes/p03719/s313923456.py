def main():
  num = list(map(int,input().split()))
  if(num[0]<=num[2] and num[2]<=num[1]):
    print('Yes')
  else:
    print('No')

main()