from collections import Counter
n = int(input()) # 入力が1つ
# map(int, input().split()) # 入力が複数
d = [int(i) for i in input().split()] # 配列で数字

m = int(input()) # 入力が1つ
# map(int, input().split()) # 入力が複数
t = [int(i) for i in input().split()]

if n < m:
    print('NO')
else:
    d_c = Counter(d)
    t_c = Counter(t)
    for k, v in t_c.items():
        n = d_c.get(k, 0)
        if n >= v:
            continue
        else:
            print('NO')
            break
    else:
        print('YES')