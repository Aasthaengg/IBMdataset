import sys


def tran(A):
    temp = []
    for i in range(len(A)):
        if i == 0:
            temp += [A[i]]
        elif A[i] != A[i - 1]:
            temp += [A[i]]
    return temp


def find(A):
    # assume consecutive elements
    dp = [1] * len(A) + [1]

    current_dic = {}

    MOD = 10**9 + 7

    for i in range(len(A)):

        if i == 0:
            current_dic[A[i]] = 1
        else:
            temp = dp[i - 1]
            if A[i] in current_dic:
                temp += current_dic[A[i]]
                temp %= MOD
                current_dic[A[i]] += dp[i - 1]
                current_dic[A[i]] %= MOD
            else:
                current_dic[A[i]] = dp[i - 1]

            dp[i] = temp
    # print(dp)
    return dp[-2] % MOD


N = int(input())
A = []
for i in range(N):
    A += [int(input())]



print(find(tran(A)))
