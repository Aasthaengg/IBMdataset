def main():
  n,m,c = list(map(int,input().split()))
  b = list(map(int,input().split()))
  a = [input().split() for l in range(n)]
  ans=0
  for i in range(0,n):
    sum=0
    for j in range(0,m):
      sum+=int(a[i][j])*b[j]
    if sum+c>0:
      ans+=1
  print(ans)
main()