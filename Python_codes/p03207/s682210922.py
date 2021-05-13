import math
def main():
  n = int(input())
  p = [int(input()) for i in range(n)]
  ans=p[0]
  max=p[0]
  for i in range(1,n):
    ans+=p[i]
    if max<p[i]:
      max=p[i]
  ans-=int(max/2)
  print(ans)
main()