def main():
  num = list(map(int,input().split()))
  ans=num[1]
  for i in range(1,num[0]):
    ans*=(num[1]-1)
  print(ans)
    
main()