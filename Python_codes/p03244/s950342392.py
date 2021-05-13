from collections import Counter


n = int(input())
v = list(map(int, input().split()))
v_former = Counter(v[::2]).most_common() + [(0, 0)]
v_latter = Counter(v[1::2]).most_common() + [(0, 0)]
if v_former[0][0] != v_latter[0][0]:
    print(n - v_former[0][1] - v_latter[0][1])
else:
    print(n - max(v_former[0][1] + v_latter[1][1], v_former[1][1] + v_latter[0][1]))
