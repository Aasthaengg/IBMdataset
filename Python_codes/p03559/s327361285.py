def main(n,a,b,c):
  import bisect
  ans=0
  for i in range(n):
    na=bisect.bisect_left(a,b[i])
    nc=n-bisect.bisect_right(c,b[i])
    ans+=na*nc
  print(ans)
if __name__=='__main__':
  n=int(input())
  a=sorted(list(map(int,input().split())))
  b=sorted(list(map(int,input().split())))
  c=sorted(list(map(int,input().split())))
  main(n,a,b,c)
