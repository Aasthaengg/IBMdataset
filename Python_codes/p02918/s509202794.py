def main(n,k,s):
  l=[0]
  for i in range(1,n):
    if s[i]==s[i-1]:
      l[-1]+=1
    else:
      l.append(0)
  print(min(n-1,sum(l)+k*2))
    
if __name__=='__main__':
  import sys
  input = sys.stdin.readline
  n,k=map(int,input().split())
  s=input()
  main(n,k,s)
