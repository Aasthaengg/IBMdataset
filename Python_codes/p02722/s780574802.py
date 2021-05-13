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

N = int(input())

# Nの約数
div1 = make_divisors(N)
# N-1の約数
div2 = make_divisors(N - 1)

#　マージして、不適な1は除く
div_set = set(div1 + div2)
div_set.remove(1)
# print(div_set)

# div_setの中身をそれぞれシミュレート
# N -> N-K　を愚直にやると時間がかかる、modK == 1となるか否かで判定
ans = 0
for div in div_set:
    tmp = N
    while tmp % div == 0:
        tmp = tmp // div

    if tmp % div == 1:
        ans += 1
print(ans)
