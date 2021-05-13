import math
def main():
  a,b = list(map(int,input().split()))
  number=b-a
  ans=0
  for i in range(1,number):
    ans+=i
  print(ans-a)
main()