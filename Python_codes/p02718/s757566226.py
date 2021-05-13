def main():
  n,m = list(map(int,input().split()))
  a = list(map(int,input().split()))
  ans=0
  num=sum(a)
  
  for i in range(0,n):
    if a[i] >= num/(4*m):
      ans+=1
      if ans==m:
        break
  if ans >= m:
    print("Yes")
  else:
    print("No")
  
main()