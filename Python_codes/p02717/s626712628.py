def main():
  a,b,c = list(map(int,input().split()))
  tmp=a
  a=b
  b=tmp
  tmp=a
  a=c
  c=tmp
  print(a,b,c)

main()