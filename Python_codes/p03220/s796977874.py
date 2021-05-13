import math
def main():
  n=int(input())
  t,a = list(map(int,input().split()))
  h = list(map(int,input().split()))
  ans = abs(a-(t-h[0]*0.006))
  ansid=0
  for i in range(1,n):
    if abs(a-(t-h[i]*0.006)) < ans :
      ans=abs(a-(t-h[i]*0.006))
      ansid=i
  print(ansid+1)
main()