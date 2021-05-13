import bisect
s = list(input())
t = list(input())
dic = {}
for i, j in enumerate(s):
    if j in dic:
        dic[j].append(i)
    else:
        dic[j] = [i]
loop = 0
if set(t) <= set(s):
    for i in range(len(t)):
        if i==0:
            idx = dic[t[0]][0]
        else:
            lis = dic[t[i]]
            idx2 = bisect.bisect_right(lis, idx)
            if idx2 == len(lis):
                loop += 1
                idx = lis[0]
            else:
                idx = lis[idx2]
    print(loop*len(s) + idx + 1)
else:
    print(-1)