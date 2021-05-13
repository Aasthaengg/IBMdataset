import collections

n=int(input())
a=list(map(int,input().split()))
num=collections.Counter(a)
cnt=num.most_common()
if cnt[0][1]<=1:
    print(0)
    exit()
else:
    if cnt[1][1]<=1:
        print(0)
        exit()
    numlis=[]
    for i in cnt:
        if i[1]>=2:
            numlis.append(i)
        else:
            break
    numlis=[list(a) for a in numlis]
    numlis.sort(reverse=True)
    if numlis[0][1]>=4:
        print(numlis[0][0]**2)
    else:
        print(numlis[0][0]*numlis[1][0])

