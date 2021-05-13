#綺麗にかけない
N = int(input())
s = [input() for i in range(N)]
M = int(input())
t = [input() for i in range(M)]
dic_s = {}
for i in set(s):
    dic_s[i] = s.count(i) 
dic_t = {}
for i in set(t):
    dic_t[i] = t.count(i)
ss=set(s)
ts=set(t)
if(ss & ts == set()):
    print(max(dic_s.values()))
else:
    dic_c = {}
    for i in ss&ts:
        dic_c[i] = dic_s[i] - dic_t[i]
    if(not (ss & (ss^ts) == set())):
        for i in ss & (ss^ts):
            dic_c[i] = dic_s[i]
    if(max(dic_c.values()) < 0):
        print(0)
    else:
        print(max(dic_c.values()))