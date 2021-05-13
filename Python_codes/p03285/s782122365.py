import math
def main():
  n = int(input())
  flg=0
  for i in range(0,int(n/7)+1):
    j=0
    while 4*j + 7*i <= n:
      if 4*j + 7*i ==n:
        flg=1
      j+=1
  if flg==1:
    print('Yes')
  else:
    print('No')
main()
