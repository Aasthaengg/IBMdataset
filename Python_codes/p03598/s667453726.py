def main():
  n = int(input())
  k = int(input())
  x = list(map(int,input().split()))
  sum=0
  for i in range(0,n):
    if abs(x[i]-0)>abs(k-x[i]):
      sum+=abs(k-x[i])*2
    else:
      sum+=abs(x[i]-0)*2
  print(sum)
    
main()