# -*- coding: utf-8 -*-
bigALlist = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
smoALlist = list('abcdefghijklmnopqrstuvwxyz')
cnt = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
while True:
    try:
        text = list(input())
        for j in range(len(bigALlist)):
            for i in text:
                if (bigALlist[j] in i) or (smoALlist[j] in i):
                    cnt[j] = cnt[j] + 1
    except EOFError:
        break
for j in range(len(bigALlist)):
    print('{0} : {1}'.format(smoALlist[j],cnt[j]))
