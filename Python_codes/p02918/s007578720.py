from collections import deque

def main():
  n,k=map(int,input().split())
  s=input()
  # maked group
  t=[]
  t.append(s[0])
  x=s[0]
  for i in range(1,n):
    if x!=s[i]:
      t.append(s[i])
      x=s[i]
  #print(t)
  
  j=0
  t=deque(t)
  while j<k:
    if len(t)<=2:
      print(n-1)
      exit(0)
    t.popleft()
    t.popleft()
    j+=1
    
  print(n-1-(len(t)-1))

  
if __name__=='__main__':
  main()