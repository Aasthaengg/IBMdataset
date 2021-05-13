import sys
input = sys.stdin.readline
def main():
  n,m=map(int,input().split())
  ab=[list(map(int,input().split())) for _ in range(m)]
  c=[0]*n
  for a,b in ab:
    c[a-1]+=1
    c[b-1]+=1
  print('NO' if len([ci for ci in c if ci%2==1])>0 else 'YES')
if __name__=='__main__':
  main()
