N,M=map(int,input().split())
XYZ=[list(map(int,input().split())) for i in range(N)]
pm={'0':1,'1':-1}
ans=0
for i in range(2**3):
  ibin = format(i, '03b')
  tmp=sorted([pm[ibin[0]]*x+pm[ibin[1]]*y+pm[ibin[2]]*z for x,y,z in XYZ],reverse=True)
  ans=sum(tmp[:M]) if ans<sum(tmp[:M]) else ans
print(ans)