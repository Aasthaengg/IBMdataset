def main(n,a):
  a=sorted([a[i]-i for i in range(n)])
  m0=a[n//2]
  m1=a[n//2-1]
  ans0,ans1=0,0
  for i in range(n):
    ans0+=abs(a[i]-m0)
    ans1+=abs(a[i]-m1)
  print(min(ans0,ans1))
if __name__=='__main__':
  import sys
  input = sys.stdin.readline
  n=int(input())
  a=list(map(int,input().split()))
  main(n,a)
