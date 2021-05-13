def main():
  import sys
  b=sys.stdin.buffer
  input=b.readline
  n=int(input())
  d=[0]*n+[1<<c-97for c in input()[:n]]
  for i in range(n-1,0,-1):d[i]=d[i+i]|d[i-~i]
  r=[]
  add=r.append
  input()
  for q,a,b in zip(*[iter(b.read().split())]*3):
    i,s=int(a)+n-1,0
    if q<b'2':
      d[i]=1<<b[0]-97
      while i:
        i>>=1
        d[i]=d[i+i]|d[i-~i]
      continue
    j=int(b)+n
    while i<j:
      if i&1:
        s|=d[i]
        i+=1
      if j&1:
        j-=1
        s|=d[j]
      i>>=1
      j>>=1
    add(bin(s).count('1'))
  print(' '.join(map(str,r)))
main()