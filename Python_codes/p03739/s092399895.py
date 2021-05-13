n=int(input())
a=list(map(int,input().split()))
mulsum=[0]*n
cnt=0
cnt2=0
buf=0
cur=0
mulsum[0]=a[0]
for i in range(n-1):
    mulsum[i+1]=mulsum[i]+a[i+1]
#print(mulsum)
i=0
pm=[]
mp=[]
while i<n:#+-+-+-...の列を目指す
    if (mulsum[i]+buf)<=0:#a[i]+buf>0になるようbufを調整
        cur=mulsum[i]+buf
        buf=1-mulsum[i]
        cnt=cnt+(1-cur)
        #pm.append(1)
    else:
        i=i
        #pm.append(mulsum[i])
    if i==n-1:
        break
    if (mulsum[i+1]+buf)>=0:#a[i+1]+buf<0になるよう調整
        cur=mulsum[i+1]+buf
        buf=-1-mulsum[i+1]
        cnt=cnt+(1+cur)
        #pm.append(-1)
    else:
        i=i
        #pm.append(mulsum[i+1])
    i=i+2
#print(pm,cnt)
buf=0
i=0
while i<n:#-+-+-+...の列を目指す
    if (mulsum[i]+buf)>=0:#a[i]+buf<0になるようbufを調整
        cur=mulsum[i]+buf
        buf=-1-mulsum[i]
        cnt2=cnt2+(1+cur)
        #mp.append(-1)
    else:
        i=i
        #mp.append(mulsum[i])
    #print(buf,cnt2)
    if i==n-1:
        break
    if (mulsum[i+1]+buf)<=0:#a[i+1]+buf>0になるよう調整
        cur=mulsum[i+1]+buf
        buf=1-mulsum[i+1]
        cnt2=cnt2+(1-cur)
        #mp.append(1)
    else:
        i=i
        #mp.append(mulsum[i+1])
    i=i+2
    #print(buf,cnt2)
#print(mp,cnt2)
print(min(cnt,cnt2))
