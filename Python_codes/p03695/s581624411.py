n = int(input())
a = list(map(int,input().split()))
c = [0,0,0,0,0,0,0,0]
at = 0
for i in range(n):
    if 1<=a[i]<=399:
        c[0]+=1
    elif 400<=a[i]<=799:
        c[1]+=1
    elif 800<=a[i]<=1199:
        c[2]+=1
    elif 1200<=a[i]<=1599:
        c[3]+=1
    elif 1600<=a[i]<=1999:
        c[4]+=1
    elif 2000<=a[i]<=2399:
        c[5]+=1
    elif 2400<=a[i]<=2799:
        c[6]+=1
    elif 2800<=a[i]<=3199:
        c[7]+=1
    else:
        at+=1
cnt=0
for i in c:
    if i >0:
        cnt+=1
ans_max=cnt+at 

if cnt==0:
    cnt=1
print(str(cnt)+" "+str(ans_max))

