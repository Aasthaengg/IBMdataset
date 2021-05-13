n,m,d=map(int,input().split())
if d==0:
    ans=((m-1)*10**7)//n
    print('{:.7g}'.format(ans/10**7))
else:
    ans=(2*(n-d)*(m-1)*10**7)//n**2
    print("{:.7g}".format(ans/(10**7)))