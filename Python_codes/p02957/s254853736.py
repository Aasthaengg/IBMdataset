def main():
  num = list(map(int,input().split()))
  if num[0]-num[1]>0 and (num[0]-num[1])%2==0:
    print(num[0]-int((num[0]-num[1])/2))
  elif num[1]-num[0]>0 and (num[1]-num[0])%2==0:
    print(num[1]-int((num[1]-num[0])/2))
  else:
    print("IMPOSSIBLE")
main()