def main():
  import sys
  input = sys.stdin.readline
  n=int(input())
  p=[0]+[int(i) for i in input().split()]+[0]
  ans=0
  for i in range(1,n+1):
    if p[i]==i:
      if p[i+1]==i+1:
        p[i+1]=i
      ans+=1
  print(ans)
if __name__=='__main__':
  main()