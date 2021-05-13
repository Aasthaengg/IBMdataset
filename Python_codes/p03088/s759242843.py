a = ['A', 'G', 'C', 'T']
l = ["GACA","GACC","GACT","AGGC","AGCA","AGCG","AGCC","AGCT","AGTC","ACGA","ACGG","ACGC","ACGT","ATGC"]
dict1_y = {}
dict1_n = {}
dict2_y = {}
dict2_n = {}
t = 3
p = 10**9+7
n = int(input())
for i in a:
    for j in a:
        for k in a:
            s = i + j + k
            dict1_y[s] = 0
            dict1_n[s] = 0
            dict2_y[s] = 0
            dict2_n[s] = 0
for i in a:
    for j in a:
        for k in a:
            s = i + j + k
            if 'AGC' in s:
                dict1_y[s] += 1
            else:
                tem1 = s[0]
                tem2 = s[1]
                new_s = tem2 + tem1 + s[2]
                if 'AGC' in new_s:
                    dict1_y[s] += 1
                else:
                    tem1 = s[1]
                    tem2 = s[2]
                    new_s = s[0] + tem2 + tem1
                    if 'AGC' in new_s:
                        dict1_y[s] += 1
                    else:
                        dict1_n[s] += 1
while t != n:
    for k,v in dict1_y.items():
        for m in a:
            key = m + k[0] + k[1]
            dict2_y[key] += v
    for k,v in dict1_n.items():
        for m in a:
            new_s = m + k
            key = m + k[0] + k[1]
            if new_s in l:
                dict2_y[key] += v
            else:
                dict2_n[key] += v
    for i in a:
        for j in a:
            for k in a:
                s = i + j + k
                dict1_y[s] = dict2_y[s] % p
                dict1_n[s] = dict2_n[s] % p
                dict2_y[s] = 0
                dict2_n[s] = 0
    t += 1
ans = 0
for v in dict1_y.values():
    ans += v % p
print((4**n - ans) % p)

