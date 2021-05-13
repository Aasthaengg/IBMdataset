def main():
  num = list(map(int,input().split()))
  if num[1]%num[0]==0:
    print( num[0]+num[1] )
  else:
    print(num[1]-num[0])
  
main()