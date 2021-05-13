def main():
  n=int(input())
  a = list(map(int,input().split()))
  ans=0
  for i in range(0,n):
    ans+=(1/a[i])
  ans=1/ans
  print(ans)

main()