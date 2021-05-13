def main():
  num = [int(input()) for i in range(5)]
  n =int(input())
  flg=0
  for i in range(0,4):
    for j in range(i,5):
      if abs(num[j]-num[i])>n :
        flg=1
        break
  if flg==0 :
    print('Yay!')
  else :
    print(':(')

main()