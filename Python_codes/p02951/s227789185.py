def main():
  num = list(map(int,input().split()))
  if num[1]+num[2]-num[0]<0:
    print(0)
  else:
    print(num[1]+num[2]-num[0])
main()