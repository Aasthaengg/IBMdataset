def main():
  n,x = list(map(int,input().split()))
  l = list(map(int,input().split()))
  bound=0
  ans=1
  for i in range(0,n):
    bound+=l[i]
    if bound <=x:
      ans+=1
  print(ans)

main()