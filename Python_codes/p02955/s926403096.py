import sys
input = sys.stdin.readline

# 約数の列挙
#############################################################
def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
#############################################################

N, K = map(int, input().split())
A = list(map(int, input().split()))

# 操作後も総和は変わらない
# 操作後にdivが公約数なら、divは総和の約数でもある
sum_A = sum(A)
div_list = make_divisors(sum_A)
ans = 1

for div in div_list:
    # divで割った余りのリストをソート
    # どこかを境に、左側は-1をして右側は+1をすると仮定する
    tmp = [a % div for a in A]
    tmp.sort()

    # 累積和
    cumsum1 = [0]
    cumsum2 = [0]
    for i in tmp:
        cumsum1.append(cumsum1[-1] + i)
        if i != 0:
            cumsum2.append(cumsum2[-1] + (div - i))
        else:
            cumsum2.append(cumsum2[-1])

    for i in range(1, N):
        cnt_minus = cumsum1[i]
        cnt_plus = cumsum2[N] - cumsum2[i]
        # 条件を満たす時、必ずどこかで等しくなる
        # （証明が理解できていないが、実験すると確かにそうなりそう）
        if cnt_minus == cnt_plus and cnt_minus <= K:
            ans = div

print(ans)
