from collections import Counter
n = int(input())
ns = list(map(int, input().split()))
dic = Counter(ns)
dic = {key:value for key, value in dic.items() if value>=2}
if len(dic) < 2:
    print(0)
else:
    sorted_dic = sorted(dic.items(), key=lambda x: x[0])
    if sorted_dic[-1][1] >= 4:
        print(sorted_dic[-1][0]**2)
    else:
        print(sorted_dic[-1][0] * sorted_dic[-2][0])
