n = int(input())
t = list(map(int, input().split()))
a = list(map(int, input().split()))
MOD = 10**9 + 7

def restor_accumulation_max(accumulation_max: list, include_0: bool) -> list:
    '''累積Maxを復元する
    Maxには逆元が存在しないので、一意に復元することはできない
    復元値の候補を[begin, end)として定義される
 
    例: accumulation_max = [3, 4, 4, 8, 8]
        include_0 = Trueのとき
        -> [(3, 4), (4, 5), (0, 5), (8, 9), (0, 9)]
        include_0 = Falseのとき
        -> [(3, 4), (4, 5), (0, 5), (8, 9), (1, 9)]
    '''
    n = len(accumulation_max)
    res = []
    init = 0 if include_0 else 1
    max_ = init
    
    for i in range(n):
        if accumulation_max[i] > max_:
            res.append((accumulation_max[i], accumulation_max[i] + 1))
            max_ = accumulation_max[i]
        else:
            res.append((init, max_ + 1))
    
    return res

li_t = restor_accumulation_max(t, False)
li_a = restor_accumulation_max(a[::-1], False)[::-1]

ans = 1
for i in range(n):
    tmp = min(li_t[i][1], li_a[i][1]) - max(li_t[i][0], li_a[i][0])
    if tmp <= 0:
        ans *= 0
    ans *= tmp
    ans %= MOD
print(ans)