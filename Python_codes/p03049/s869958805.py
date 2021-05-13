n= int(input())
bdic = {'A':0,'B':1,'O':2}
aot = [[0 for i in range(3)] for i in range(3)]
ans=0
for i in range(n):
    s=input()
    subab=0
    for i in range(len(s)-1):
        if s[i]=='A' and s[i+1]=='B':subab+=1
    ans += subab
    f = 'O' if not s[0]  in bdic.keys() else s[0]
    l = 'O' if not s[-1] in bdic.keys() else s[-1]
    aot[bdic[f]][bdic[l]]+=1

oa = aot[bdic['O']][bdic['A']]+aot[bdic['A']][bdic['A']]
bo = aot[bdic['B']][bdic['O']]+aot[bdic['B']][bdic['B']]
ab = aot[bdic['A']][bdic['B']]
ba = aot[bdic['B']][bdic['A']]

if   oa==0 and bo==0:ans+=max(0,ba-1)
elif oa==0 and bo!=0:ans+=min(bo,ba)+max(0,ba-bo)
elif bo==0 and oa!=0:ans+=min(oa,ba)+max(0,ba-oa)
else:                ans+=min(oa,bo)+ba
print(ans)