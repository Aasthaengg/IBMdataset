def main():
  n=int(input())
  a=list(map(int,input().split()))
  b=list(map(int,input().split()))
  c=[a[i]-b[i] for i in range(n)]
  c0=sum([ci for ci in c if ci>0])
  c1=sum([-2*((ci+2-1)//2) for ci in c if ci<0])
  print('Yes' if c1>=2*c0 else 'No')
if __name__=='__main__':
  main()
