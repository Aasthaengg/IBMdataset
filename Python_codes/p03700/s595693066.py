import copy

N,A,B=map(int,input().split())
h=[]
for i in range(0,N):
    H=int(input())
    h.append(H)

h.sort()

def condition(num):
    testlist=copy.copy(h)
    for i in range(0,N):
        testlist[i]-=B*num
    count=0
    for i in range(0,N):
        if testlist[i]>0:
            if testlist[i]%(A-B)!=0:
                count+=testlist[i]//(A-B)+1
            else:
                count+=testlist[i]//(A-B)
    return num>=count

start=1
end=10**15
while end-start>1:
    test=(end+start)//2
    if condition(test):
        end=test
    else:
        start=test

if condition(start):
    print(start)
else:
    print(end)
