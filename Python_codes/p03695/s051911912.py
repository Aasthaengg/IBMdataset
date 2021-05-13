N = int(input())
c = list(map(int,input().split()))
b = [0]*8
cnt = 0
for a in c:
    if 0<a<400:
        b[0]=1
    elif 399<a<800:
        b[1]=1
    elif 799<a<1200:
        b[2]=1
    elif 1199<a<1600:
        b[3]=1
    elif 1599<a<2000:
        b[4]=1
    elif 1999<a<2400:
        b[5]=1
    elif 2399<a<2800:
        b[6]=1
    elif 2799<a<3200:
        b[7]=1
    else:
        cnt += 1
print(max(1, b.count(1)), end = " ")
print(b.count(1) + cnt)