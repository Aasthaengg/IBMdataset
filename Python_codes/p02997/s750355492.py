n,k=map(int,input().split())
def ans():
  m=n
  if k>((n-1)*(n-2)//2):
    print(-1)
    return
  else:
    c=(n-1)*(n-2)//2-k
    a=[]
    for i in range(2,n+1):
      a.append([1,i])
    if c>0:
      for i in range(2,n+1):
        for j in range(i+1,n+1):
          a.append([i,j])
          c-=1
          if c==0:
            break
        if c==0:
          break
    print(len(a))
    for i in range(len(a)):
      print(a[i][0],a[i][1])
ans()