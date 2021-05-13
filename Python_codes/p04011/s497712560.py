def main():
 num =  [int(input()) for i in range(4)]
 price=0
 for i in range(0,num[0]):
  if i< num[1] :
   price+=num[2]
  else:
   price+=num[3]
 print(price)

main()