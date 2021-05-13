n,y=map(int,input().split())
judge=False
for i in range(n+1):
    if judge==True:
      break
    for j in range(n-i+1):
        if judge==True:
          break
        k=n-i-j
        if 1000*i+5000*j+10000*k==y:
            print(k,j,i)
            judge=True
            break
if judge==False:
    print(-1,-1,-1)