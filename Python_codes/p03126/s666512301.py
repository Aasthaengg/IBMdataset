import math
def main():
  n,m = list(map(int,input().split()))
  alist=[[]]
  for i in range(0,n):
    alist.append(list(map(int,input().split())))
  ans=set(alist[1][1:])
  for i in range(2,n+1):
    ans=ans & set(alist[i][1:])
  print(len(ans))
main()