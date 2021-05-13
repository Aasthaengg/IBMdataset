from collections import defaultdict as dd
N,T = map(int,input().split())
a = list(map(int,input().split()))
dic=dd(int)
mi = a[0]
for i in range(1,N):
    if a[i] < mi:
        mi = a[i]
    else:
        profit = a[i]-mi
        dic[profit] += 1
res = dic[max(dic.keys())]
print(res)