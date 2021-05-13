list_n=[0]+list(map(int,input()))
l = len(list_n)

pay=0
back=0
for i in range(l-1,-1,-1):
    #l-1から0まで
    now = list_n[i]
    if now in [0,1,2,3,4] or (now == 5 and list_n[i-1]<5):
        pay+=now
        list_n[i]=0
    elif now in [6,7,8,9] or (now == 5 and list_n[i-1]>=5):
        back+=10-now
        list_n[i]=0
        list_n[i-1] +=1
    elif now==10:
        list_n[i]=0
        list_n[i-1] +=1
print(pay+back)