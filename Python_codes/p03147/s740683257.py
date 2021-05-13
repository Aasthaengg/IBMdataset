N=int(input())
S=list(map(int,input().split()))

searchmin=10**4
pos=0
start=0
end=0
lenS=len(S)
count=0

def startendsearch():
    atta=False
    start=0
    end=0
    for i in range(lenS):
        if S[i]!=0 and atta==False:
            start=i
            atta=True
        if S[i]!=0 and atta==True:
            end=i
        if S[i]==0 and atta==True:
            break
    
    if atta==True:
        return start,end
    else:
        return 200,200
while sum(S)>0:
    s,e= startendsearch()
    
    #print(s,e)
    for i in range(s,e+1):
        S[i]-=1
        
    #print(S)
    count+=1
print(count)