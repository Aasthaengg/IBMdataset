n = int(input())
a = list(map(int,input().split()))
dic = {}
over = 0
color = 8
for i in range(n):
    if a[i]<400:
        dic.setdefault(400,0)
        dic[400] += 1
    elif a[i]<800:
        dic.setdefault(800,0)
        dic[800] += 1
    elif a[i]<1200:
        dic.setdefault(1200,0)
        dic[1200] += 1
    elif a[i]<1600:
        dic.setdefault(1600,0)
        dic[1600] += 1
    elif a[i]<2000:
        dic.setdefault(2000,0)
        dic[2000] += 1
    elif a[i]<2400:
        dic.setdefault(2400,0)
        dic[2400] += 1
    elif a[i]<2800:
        dic.setdefault(2800,0)
        dic[2800] += 1
    elif a[i]<3200:
        dic.setdefault(3200,0)
        dic[3200] += 1
    else:
        over += 1

if over > 0:
    if len(dic)==0:
        print(1,over)
    else:
        print(len(dic),len(dic)+over)
else:
    print(len(dic),len(dic))