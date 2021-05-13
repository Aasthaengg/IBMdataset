def main():
  num = list(map(int,input().split()))
  if num[0] in [1,3,5,7,8,10,12] :
    if num[1] in [1,3,5,7,8,10,12] :
      print('Yes')
    else:
      print('No')
  elif num[0] in [4,6,9,11] :
    if num[1] in [4,6,9,11] :
      print('Yes')
    else:
      print('No')
  elif num[0] ==2 :
    if num[1] ==2 :
      print('Yes')
    else:
      print('No')
      
main()