def main():
  n,p=map(int,input().split())
  s=input()
  if 10%p==0:
    print(sum(i for i,x in enumerate(s,1) if int(x)%p==0))
    exit()
  s=s[::-1]
  x=[0]*p
  x[0]=1
  a,t=0,1
  for i in range(n):
    a=(a+int(s[i])*t)%p
    x[a]+=1
    t=(t*10)%p
  ans=sum([i*(i-1)//2 for i in x])
  print(ans)
if __name__=='__main__':
  main()