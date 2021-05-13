def main():
  num = list(map(int,input().split()))
  min=num[0]+num[1]
  if min>num[1]+num[2]:
    min=num[1]+num[2]
  if min>num[0]+num[2]:
    min=num[0]+num[2]
  print(min)

main()