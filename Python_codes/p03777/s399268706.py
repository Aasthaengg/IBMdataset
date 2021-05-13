def main():
  string = list(map(str,input().split()))
  if string[0]=='H':
    print(string[1])
  else:
    if string[1]=='H':
      print('D')
    else:
      print('H')

main()