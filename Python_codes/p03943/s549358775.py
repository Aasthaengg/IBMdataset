def main():
 num = list(map(int,input().split()))
 if (num[0]+num[1])==num[2] or (num[0]+num[2])==num[1] or(num[1]+num[2])==num[0] :
  print('Yes')
 else:
   print('No')
 
main()