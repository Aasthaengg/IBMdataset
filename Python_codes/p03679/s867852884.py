def main():
  num = list(map(int,input().split()))
  if num[2]<=num[1]:
    print('delicious')
  elif num[0] >= num[2]-num[1]:
    print('safe')
  else:
    print('dangerous')
      
main()