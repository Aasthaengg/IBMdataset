n = int(input())
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))
"""
先頭からなめていって、
A. ai < biなら対処が必要⇒変更確定
B. ai == biなら変更不要で確定
C. ai > biなら他に融通する可能性あり⇒保留
Aのケースの不足数の総和を計算し、Cの差分の大きいものから順に使っていく。
Cのheapqを作成するのかな？いったんリストでやってみるか
"""
if sum(aa) < sum(bb):
    print(-1)
else:
    total_diff = 0
    margin = []
    modified = 0
    for i in range(n):
        if aa[i] < bb[i]:
            modified += 1
            total_diff += bb[i] - aa[i]
        elif aa[i] > bb[i]:
            margin.append(aa[i]-bb[i])
    margin.sort(reverse=True)
    while total_diff > 0:
        modified += 1
        t = margin.pop(0)
        total_diff -= t
    print(modified)
