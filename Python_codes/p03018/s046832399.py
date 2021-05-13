S=input().replace("BC","#")

cnt,point=0,0
for i in range(len(S)):
    if S[i]=="A":point +=1
    elif S[i]=="#":cnt +=point
    else:point=0
print(cnt)