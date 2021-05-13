import sys
input = sys.stdin.readline
def main():
  n=int(input())
  if n==0:
    print(0)
    exit()
  s=1 if n>0 else 0
  n=abs(n)
  for j in range(s,31,2):
    if ((n>>j) & 1): #立っているビットのところで処理が走る
      n+=pow(2,j+1)
  print(bin(n)[2:])
if __name__=='__main__':
  main()
