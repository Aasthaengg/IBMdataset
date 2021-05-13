def main():
  num = [int(input()) for i in range(5)]
  min_num=num[0]%10
  last_index=0
  ans=0
  for i in range(1,len(num)):
    if( num[i]%10 < min_num and num[i]%10!=0) or min_num==0 :
      min_num=num[i]%10
      last_index=i
  
  for i in range(0,len(num)):
    if i==last_index or num[i]%10==0:
      ans+=num[i]
    else:
      ans+=((int(num[i]/10)+1)*10)
  print(ans)

main()