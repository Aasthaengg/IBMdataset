# https://atcoder.jp/contests/abc114/tasks/abc114_d

from collections import defaultdict

def solve():
    n = int(input())
    
    # 32400 = 2^4 3^4 5^2
    # => 5 x 5 x 3 = 75
    # 75の分割分だけ持てば良い

    # 10! = 1 x 2 x 3 x 4 x 5 x 6 x 7 x 8 x 9 x 10
    # 10! = 1 x 2 x 3 x (2x2) x 5 x (2x3) x 7 x (2x2x2) x (3x3) x (2x5)
    # 10!の約数 nCk個取ってきた積で割り切れる
    # 1を除いてちょうど74個あるかどうか

    # 2 ~ n までの素因数分解
    e = [0] * (n + 1)
    for i in range(2, n + 1):
        cur = i
        for j in range(2, i + 1):
            while cur % j == 0:
                e[j] += 1
                cur //= j
    
    def num(m):
        return len(list(filter(lambda x: x >= m - 1, e)))

    v1 = num(75) # 75乗を作れるやつ
    v2 = num(25) * (num(3) - 1) # 25乗 x 3乗 (25乗に使った分を含まない)
    v3 = num(15) * (num(5) - 1) # 15乗 x 5乗
    v4 = num(5) * (num(5) - 1) * (num(3) - 2) // 2 # 5乗 x 5乗(-1) x 3乗(-2)
    ans = v1 + v2 + v3 + v4
    # print(e)
    # print(v1)
    # print(v2)
    # print(v3)
    # print(v4)
    print(ans)

if __name__ == '__main__':
    solve()