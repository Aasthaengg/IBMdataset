from collections import Counter
def comb(a, b):
    if b > a:
        return 0
    tmp1 = 1
    tmp2 = 1
    for i in range(b):
        tmp1 *= (a-i)
        tmp2 *= (b-i)
    return tmp1//tmp2

N = int(input())
A = [int(i) for i in input().split()]
count_dict = Counter(A)
# いったん引かなかった場合の総和を計算しておいて、あとで一回分引いて足すをする
comp_sum = 0
for key in count_dict.keys():
    comp_sum += comb(count_dict[key], 2)

# 引かれるやつとそうじゃないのをそれぞれメモしとく
for i in range(N):
    print(comp_sum + comb(count_dict[A[i]]-1, 2) -  comb(count_dict[A[i]], 2))
