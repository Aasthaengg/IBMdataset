def main():
  num = list(map(int,input().split()))
  if num[0]*num[2]<=num[1]:
    print( num[2] )
  else:
    print(int(num[1]/num[0]))

main()