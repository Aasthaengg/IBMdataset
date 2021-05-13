s = input()
s_li = list(s)
k = int(input())

alp = list('abcdefghijklmnopqrstuvwxyz')
moji_li = []
count_li = []
for ss in s_li:
    ind = alp.index(ss)
    moji_li.append(alp.index(ss))
    count_li.append(26 - alp.index(ss))
for i,c in enumerate(count_li):
    #print(i,len(count_li)-1)
    if i == len(count_li)-1:
        moji_li[i]+= k
        break
    else:
        if c == 26:
            continue
        if c<=k:
            k-=c
            moji_li[i]=0
ans = ''
#print('count_li',count_li)
#print(moji_li)
for m in moji_li:
    ans += alp[m%26]
print(ans)