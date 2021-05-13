def main():
  n=int(input())
  p = list(map(int,input().split()))
  ans=0
  for i in range(0,n-2):
    if max(p[i:i+3])!=p[i+1] and min(p[i:i+3])!=p[i+1]:
      ans+=1
  print(ans)
main()