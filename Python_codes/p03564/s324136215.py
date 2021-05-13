def main():
  n,k = [int(input()) for i in range(2)]
  ans=1
  for i in range(0,n):
    if ans>k:
      ans+=k
    else:
      ans*=2
  print(ans)
main()
