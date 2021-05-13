count = int(input())

pls_flg = False
mns_flg = False
srt_flg = True
tmp = input().split()
num = []
work_max = 0
work_min = 0
index_max = 0
index_min = 0

for i in range(count):
    if int(tmp[i])>0:
        num.append(int(tmp[i]))
        pls_flg = True
        if work_max < num[i]:
            work_max = num[i]
            index_max = i
    elif int(tmp[i])<0:
        num.append(int(tmp[i]))
        mns_flg = True
        if abs(work_min) < abs(num[i]):
            work_min = num[i]
            index_min = i
    else:
        num.append(int(tmp[i]))
    
    if srt_flg and i > 0:
        if num[i-1] > num[i]:
            srt_flg = False

if srt_flg:
    print(0)
else:
    if pls_flg and not mns_flg:
        print(count-1)
        for j in range(count-1):
            print(str(j+1)+" "+str(j+2))
    elif not pls_flg and mns_flg:
        print(count-1)
        for j in range(count-1):
            print(str(count-j)+" "+str(count-1-j))
    elif pls_flg and mns_flg:
        print(2*count-1)
        if work_max >= abs(work_min):
            for x in range(count):
                print(str(index_max+1)+" "+str(x+1))
            for y in range(count-1):
                print(str(y+1)+" "+str(y+2))
        else:
            for x in range(count):
                print(str(index_min+1)+" "+str(x+1))
            for y in range(count-1):
                print(str(count-y)+" "+str(count-y-1))
    else:
        print(0)