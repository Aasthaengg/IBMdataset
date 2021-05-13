n=int(input())
S=input()
anslist=[]
c=0
#3けたの暗証番号なので000~999までの最大1000通り
for i in range(1000):
    c=0
    if i<10:
        i="00"+str(i)
    elif i<100:
        i="0"+str(i)
    else:
        i=str(i)
    tmp=""
    j=0
    while j<n:
        if S[j]==i[0]:
            tmp+=S[j]
            j+=1
            break
        j+=1
    while j<n:
        if S[j]==i[1]:
            tmp+=S[j]
            j+=1
            break
        j+=1
    while j<n:
        if S[j]==i[2]:
            tmp+=S[j]
            j+=1
            break
        j+=1
    if tmp==i:
        anslist.append(tmp)
                        
#print(anslist)
print(len(anslist))