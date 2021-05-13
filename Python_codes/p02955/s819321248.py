n, k = map(int, input().split())
A = list(map(int, input().split()))

all_sum = sum(A)

# 答え（約数）の候補リスト
divisors = []

# 全整数を足した値の約数が答えの候補
for i in range(1,all_sum+1):
    if i * i > all_sum:
        break
    if all_sum % i != 0:
        continue
    divisors.append(i)
    if all_sum // i != i:
        divisors.append(all_sum // i)

# 大きい値から順番に探索
divisors.sort(reverse=True)

def ok(d):
    # 答えの候補dで全値を割った余り
    a = [x % d for x in A]
    
    # 値を大きくする対象の整数の数（dを基準として、それより大きい/小さいの数を求める）
    move = n - sum(a) // d
    a.sort()
    # dで割り切れる値まで変化させる（大きく/小さくする）対象の整数について、
    # 目標の値まで値を変化させる合計値が、k以内に収まるか？
    return sum(a[:move]) <= k

for d in divisors:
    if ok(d):
        print(d)
        break