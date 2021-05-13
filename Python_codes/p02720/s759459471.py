K = int(input())
lunlun =[]
luncnt = 0

def SUM(num,cnt,keta):
    global luncnt
    if luncnt > 10**5:
        return
    if int(cnt) > int(keta):
        lunlun.append(int(num))
        luncnt += 1
        return


    if len(num) == 0:
        for i in range(1,10):
            SUM(num+str(i),str(int(cnt)+1),keta)
    else:
        min = int(num[(len(num)-1)])-1
        max = min + 3
        for i in range(min,max):
            if i < 0 or i > 9:
                continue
            SUM(num+str(i),str(int(cnt)+1),keta)

keta = 0
while True:
    SUM('','0',str(keta))
    if luncnt > 10**5:
        break
    keta += 1

print(lunlun[K-1])