n,m=map(int,input().split())
ansct=0
ansflag=[0]*n
miss=[0]*n
missct=0
for i in range(m):
    p,s=map(str,input().split())
    if (s=='AC')and(ansflag[int(p)-1]==0):
        ansflag[int(p)-1]=1
        ansct+=1
        missct+=miss[int(p)-1]
    elif ansflag[int(p)-1]==0:
        miss[int(p)-1]+=1
print(str(ansct)+' '+str(missct))