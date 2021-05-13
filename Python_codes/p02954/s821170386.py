from itertools import accumulate
S = input()
ans = [0]*len(S)
RLgr = []
R = 0
L = 0
RL = "R"
for i in range(len(S)):
    if S[i] == RL:
        if S[i] == "R":
            R += 1
        else:
            L += 1
    else:
        if RL == "R":
            RLgr.append(R)
            R = 0
            RL = "L"
            L+=1
        else:
            RLgr.append(L)
            L = 0
            RL = "R"
            R+=1
RLgr.append(L)
RLsum = list(accumulate(RLgr))
for i in range(0,len(RLgr)-1,+2):
    a=RLgr[i]//2
    b=RLgr[i+1]//2
    ans[RLsum[i]-1]=b+RLgr[i]-a
    ans[RLsum[i]]=a+RLgr[i+1]-b

for i in ans:
    print(i,end=" ")
