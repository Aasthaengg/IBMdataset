def main():
  n=int(input())
  a=sorted(list(map(int,input().split())))
  mod=pow(10,9)+7
  if n%2==0:
    b=[2*(i//2)+1 for i in range(n)]
    if  not all(a[i]==b[i] for i in range(n)):
      ans=0
    else:
      ans=pow(2,n//2,mod)
  else:
    b=[0]+[2*(i//2) for i in range(2,n+1)]
    if not all(a[i]==b[i] for i in range(n)):
      ans=0
    else:
      ans=pow(2,n//2,mod)
  print(ans)
if __name__ == '__main__':
    main()