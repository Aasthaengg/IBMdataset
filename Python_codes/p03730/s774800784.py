def main():
  a,b,c = list(map(int,input().split()))
  flg=0
  i=0
  while i<=a:
    if (b*i+c) % a==0:
      flg=1
    i+=1
  if flg==1:
    print("YES")
  else:
    print("NO")
  
main()