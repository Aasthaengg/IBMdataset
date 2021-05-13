import numpy as np
n=int(input())
a=list(map(int,input().split()))
b=a.copy()
b.insert(0,0)

#連続する重複を除外
arr=np.array(b)
diff=np.diff(arr)
arr2=np.array(a)
aa=arr2[np.nonzero(diff)]

aaa=aa.tolist()
point=[]
cnt=1
if len(aaa)<=2:
    print(1)
else:
    for i in range(len(aaa)-2):
        if (aaa[i+1]-aaa[i])*(aaa[i+2]-aaa[i+1])<0:
            cnt+=1
            point.append(i)
    
    if len(point)>1:
        for i in range(1,len(point)):
            if point[i]-1==point[i-1]:
                point[i]-=1
                cnt-=1
    print(cnt)