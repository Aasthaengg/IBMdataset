def main():
  num = list(map(int,input().split()))
  if (num[0] in [1,3,5,7,8,10,12] and num[1] in [1,3,5,7,8,10,12] ) or (num[0] in [4,6,9,11] and num[1] in [4,6,9,11] ) or (num[0] ==2 and num[1] ==2):
    print('Yes')
  else:
    print('No')
      
main()