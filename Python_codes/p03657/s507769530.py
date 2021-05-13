def main():
  num = list(map(int,input().split()))
  if num[0]%3==0 or num[1]%3==0 or (num[0]+num[1])%3==0:
    print('Possible')
  else:
    print('Impossible')
    
main()