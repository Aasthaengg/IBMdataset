from scipy.special import comb
N, P = map(int, input().split())
A = list(map(int, input().split()))
MAX_C = 100

# def comb_dp():
#     """
#     dpテーブルを作ってnCkを計算.
#     modのpは素数でなくてよい.
#     1 <= k <= n <= 2000程度
#     O(MAX_C ** 2).
#     """
#     Com = [[0]*MAX_C for _ in range(MAX_C)]
#     for i in range(1, MAX_C):
#         # iC0 = 1
#         Com[i][0] = 1
#         for j in range(1, MAX_C):
#             # iCj = i-1_C_j-1 + i-1_C_j mod p
#             Com[i][j] = (Com[i-1][j-1] + Com[i-1][j])
        
#     return Com
# Com = comb_dp()
# print(Com[2][1])
# print(Com[2][2])
if P == 0:
    is_even = [A[i]%2==0 for i in range(N)]
    num_e = is_even.count(True)
    num_o = N-num_e
    tmp1 = 0
    tmp2 = 0
    for i in range(0, num_e+1):
        tmp1 += comb(num_e, i, exact=True)
    for i in range(0, num_o+1, 2):
        tmp2 += comb(num_o, i, exact=True)
    print(tmp1*tmp2)
else:
    is_even = [A[i]%2==0 for i in range(N)]
    num_e = is_even.count(True)
    num_o = N-num_e
    tmp1 = 0
    tmp2 = 0
    for i in range(0, num_e+1):
        tmp1 += comb(num_e, i, exact=True)
    for i in range(1, num_o+1, 2):
        tmp2 += comb(num_o, i, exact=True)
    print(tmp1*tmp2)
