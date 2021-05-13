def main():
  n,x = list(map(int,input().split()))
  min=1000
  sum=0
  for i in range(0,n):
    m= int(input())
    sum+=m
    if min>m:
      min=m
  ans=n+int((x-sum)/min)
  print(ans)
main()
