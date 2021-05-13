from collections import Counter


n = int(input())
v = list(map(int, input().split()))
v_former = sorted([(v, k) for k, v in Counter(v[::2]).items()], reverse=True)
v_latter = sorted([(v, k) for k, v in Counter(v[1::2]).items()], reverse=True)
if len(v_former) == 1 and len(v_latter) == 1:
    if v_former[0][1] != v_latter[0][1]:
        print(0)
    else:
        print(n // 2)
elif v_former[0][1] != v_latter[0][1]:
    print(n - v_former[0][0] - v_latter[0][0])
elif len(v_former) == 1:
    print(n - v_former[0][0] - v_latter[1][0])
elif len(v_latter) == 1:
    print(n - v_former[1][0] - v_latter[0][0])
else:
    print(n - max(v_former[0][0] + v_latter[1][0], v_former[1][0] + v_latter[0][0]))
