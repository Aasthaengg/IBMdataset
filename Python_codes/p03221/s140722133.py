import bisect

N, M = map(int, input().split())  # 県数, 市数
birth_list = []  # 県番号, 誕生年のペア
pref_year_list = {}
for i in range(M):
    pi, yi = map(int, input().split())  # 市の県番号, 市の誕生年
    birth_list.append((pi, yi))
    if pi in pref_year_list:
        pref_year_list[pi].append(yi)
    else:
        pref_year_list[pi] = [yi]
for k in pref_year_list.keys():
    pref_year_list[k] = list(sorted(pref_year_list[k]))


for pi, yi in birth_list:
    # 県番号,年から登録順を逆引き
    year_list = pref_year_list[pi]
    i = bisect.bisect(year_list, yi)
    print("%06d%06d" % (pi, i))
