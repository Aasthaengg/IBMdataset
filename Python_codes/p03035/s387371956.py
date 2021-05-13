def main():
  num = list(map(int,input().split()))
  if num[0]<=5:
    print(0)
  elif num[0]>=13:
    print(num[1])
  else :
    print(int(num[1]/2))

main()