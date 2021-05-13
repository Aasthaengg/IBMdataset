import math
con=math.sqrt(3)/2

def gohho(da):
    ans=[]
    n=len(da)
    for i in range(n-1):
        ans.append(da[i])
        ans.append([(da[i][0]*2+da[i+1][0])/3,(da[i][1]*2+da[i+1][1])/3])
        ans.append([(da[i][0]*2+da[i+1][0])/3+(da[i+1][0]-da[i][0])*0.5/3-(da[i+1][1]-da[i][1])*con/3,(da[i][1]*2+da[i+1][1])/3+(da[i+1][0]-da[i][0])*con/3+(da[i+1][1]-da[i][1])*0.5/3])
        ans.append([(da[i][0]+da[i+1][0]*2)/3,(da[i][1]+da[i+1][1]*2)/3])
    ans.append(da[-1])
    return ans

n=int(input())
da=[[0,0],[100,0]]
for i in range(n):
    da=gohho(da)
for i in da:
    print(i[0],i[1])

