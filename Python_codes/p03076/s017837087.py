from math import ceil
time=[int(input()) for i in range(5)]
amari=[]
ans=0
for i in time:
    if i%10!=0:
        amari.append([i%10,ceil(i/10),i])

    else:
        amari.append([114514,ceil(i/10),i])
amari.sort()
amari.reverse()
for i in range(len(amari)):
    ans+=amari[i][1]*10
ans-=amari[-1][1]*10
ans+=amari[-1][2]
print(ans)