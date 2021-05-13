from itertools import groupby

N=int(input())
S=input()
def condition(num):
    if num==0:
        return True
    else:
        flag=0
        data=[]
        for i in range(0,N-num+1):
            data.append([S[i:i+num],i])
        data.sort()
        partdata=[data[i][0] for i in range(0,len(data))]
        partdata=groupby(partdata)
        subdata=[]
        for key,group in partdata:
            g=len(list(group))
            subdata.append(g)
        s=0
        t=subdata[0]-1
        if len(subdata)==1:
            if data[t][1]-data[s][1]>=num:
                flag=1
        for i in range(0,len(subdata)-1):
            if data[t][1]-data[s][1]>=num:
                flag=1
            s=t+1
            t=t+subdata[i+1]
        if data[t][1]-data[s][1]>=num:
            flag=1
        return flag==1

start=0
end=N
while end-start>1:
    test=(end+start)//2
    if condition(test):
        start=test
    else:
        end=test
if condition(end):
    print(end)
else:
    print(start)
