def main():
  NUM=list(map(int,input().split()))
  H=NUM[0]
  W=NUM[1]
  num=list(map(int,input().split()))
  h=num[0]
  w=num[1]
  print(H*W-(h*W)-(H*w)+w*h)

main()