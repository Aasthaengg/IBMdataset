from collections import defaultdict
N = int(input())
al = list(map(int,input().split()))
cnt = 0
dic = defaultdict(int)
for i in al:
    if 1<= i <= 399:
        dic['gray'] += 1
    elif 400 <= i <= 799:
        dic['brown'] += 1
    elif 800 <= i <= 1199:
        dic['green'] += 1
    elif 1200 <= i <= 1599:
        dic['cyan'] += 1
    elif 1600 <= i <= 1999:
        dic['blue'] += 1
    elif 2000 <= i <= 2399:
        dic['yellow'] += 1
    elif 2400 <= i <= 2799:
        dic['orange'] += 1
    elif 2800 <= i <= 3199:
        dic['red'] += 1
    else:
        cnt += 1


ansmax = len(dic.keys()) + cnt
if ansmax > N:
    ansmax = N


ansmin = len(dic.keys())
if ansmin == 0 and cnt >= 1:
    ansmin = 1

print(ansmin,ansmax)