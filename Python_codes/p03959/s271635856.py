#coding=UTF-8

N=int(input())
mozir=input()
hyo=mozir.split(' ')

Rec_LTR=[int(mono) for mono in hyo]

mozir=input()
hyo=mozir.split(' ')

Rec_RTL=[int(mono) for mono in hyo]

LTR_hani=[]
highest=0
for idx in range(0,N,1):
    if Rec_LTR[idx]>highest:
        highest=Rec_LTR[idx]
        LTR_hani.append([highest,highest])
    else:
        LTR_hani.append([highest,1])

RTL_hani=[None]*N
highest=0
for idx in range(N-1,-1,-1):
    if Rec_RTL[idx]>highest:
        highest=Rec_RTL[idx]
        RTL_hani[idx]=[highest,highest]
    else:
        RTL_hani[idx]=[highest,1]

#concat
ans=1
hou=1000000007
for idx in range(0,N,1):
    # prod set
    ue=min(RTL_hani[idx][0],LTR_hani[idx][0])
    shita=max(RTL_hani[idx][1],LTR_hani[idx][1])
    ans=(ans*max((ue-shita+1),0))%hou

print(ans)
