from scipy.special import comb
n, p = map(int, input().split())
A = list(map(int, input().split()))
cnt_o = len([a for a in A if a%2 == 1])
cnt_e = n - cnt_o
sum_comb_o = 0  # 奇数からとる組み合わせの和
for i in range(n+1):
    if p == 0 and i%2 == 0:
        sum_comb_o += comb(cnt_o, i, exact=True)
    elif p == 1 and i%2 == 1:
        sum_comb_o += comb(cnt_o, i, exact=True)
print(2**cnt_e * sum_comb_o)