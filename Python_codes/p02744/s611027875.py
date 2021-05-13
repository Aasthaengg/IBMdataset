'''
Created on 2020/09/09

@author: harurun
'''

def dfs(s,t,N):
  if len(s)==N:
    print(s)
  else:
    c=97
    while c<=ord(t):
      if c==ord(t):
        dfs(s+chr(c),chr(ord(t)+1),N)
      else:
        dfs(s+chr(c),t,N)
      c+=1
  return

def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write

  N=int(pin())
  dfs("",'a',N)
  return

main()

##解説AC
