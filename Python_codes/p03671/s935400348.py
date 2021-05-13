def main():
  num = list(map(int,input().split()))
  if num[0]+num[1]>num[0]+num[2]:
    if num[0]+num[2]>num[1]+num[2]:
      print(num[1]+num[2])
    else:
      print(num[0]+num[2])
  else:
    if num[0]+num[1]>num[1]+num[2]:
      print(num[1]+num[2])
    else:
      print(num[0]+num[1])
    
main()