def main():
  n = int(input())
  sum=0
  for i in range(0,n):
    l,r=list(map(int,input().split()))
    sum+=r-l+1
  print(sum)
main()