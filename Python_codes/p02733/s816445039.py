h,w,k=map(int,input().split())

s=[input() for _ in range(h)]

#hが短いのでhはbit全探索

count=10**9
#print(s)
for i in range(2**(h-1)):
    cnt=bin(i).count("1")

    #yには何行目で割るかが配列ではいる
    y=[]
    for j in range(h-1):
        if (i>>j) &1:
            y.append(j)
    y.append(h-1)
    ruiseki=[0]*(cnt+1)
    #print("y>>>>",y)
    test=0
    flag2=0
    for xx in range(w):
        yyy=0
        flag=0
        for index,yy in enumerate(y):
            while yyy<=yy:
                if s[yyy][xx]=="1":
                    ruiseki[index]+=1
                yyy+=1
        #print(max(ruiseki))
        if max(ruiseki)>k:
            #print("reset")
            cnt+=1
            yyy=0
            ruiseki=[0]*(bin(i).count("1")+1)
            for index,yy in enumerate(y):
                while yyy<=yy:
                    if s[yyy][xx]=="1":
                        ruiseki[index]+=1
                    yyy+=1
            if max(ruiseki)>k:
                #print("kore ha dame")
                flag2=1
                break
        #print(xx,ruiseki)
        #print("count:",cnt)
    if flag2==0:
        count=min(count,cnt)
print(count)



        


    
        


