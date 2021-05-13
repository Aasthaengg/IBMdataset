def main():
  a,b= list(map(int,input().split()))
  ans=1
  num=0
  while ans<b:
    num+=1
    ans+=a
    ans-=1
  print(num)

main()