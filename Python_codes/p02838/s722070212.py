import sys
input = sys.stdin.readline
def main():
  n=int(input())
  #a=list(map(lambda x:list(map(int,list(bin(int(x))[2:]))),input().split()))
  a=list(map(int,input().split()))
  mod=pow(10,9)+7
  bit=[0]*61
  for ai in a:
    for j in range(61):
      if ((ai>>j)&1):
        bit[j]+=1
  ans=0
  for i in range(61):# 2^iの位
    ans+=(pow(2,i,mod)*bit[i]*(n-bit[i]))%mod
    ans%=mod
  print(ans)
if __name__=='__main__':
  main()