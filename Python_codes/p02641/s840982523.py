def abc170_c_0():
    def solve():
        x, n = map(int, input().split(' '))
        if n == 0:
            return x

        p = list(map(int, input().split(' ')))

        search_range_min = min(min(p), x) - 1
        search_range_max = max(max(p), x) + 1
        search_values = [i for i in range(search_range_min, search_range_max + 1) if i not in p]

        check_dict = {}

        for i in search_values:
            # 絶対値が小さいものを調べるので差の絶対値を格納
            check_dict[i] = abs(x - i)

        return min(check_dict, key=check_dict.get)
    print(solve())

def abc170_c_1():
    """
    もうちょいコンパクトに書いてみる
    """
    def solve():
        x, n = map(int, input().split(' '))
        if n == 0:
            return x

        p = list(map(int, input().split(' ')))

        search_range_min = min(min(p), x) - 1
        search_range_max = max(max(p), x) + 1
        search_values = [i for i in range(search_range_min, search_range_max + 1) if i not in p]

        # min関数のkeyにxとの差の絶対値を直接渡してその値の最小値を取得してしまう。
        ans = min(search_values, key=lambda a: (abs(a - x), x))

        # こっちはたぶん絶対値の差が同じ時にリストの先にあるほうをとってしまうので結果バグっている気がする
        # ans = min(search_values, key=lambda a: abs(a - x))

        return ans

    print(solve())

if __name__ == '__main__':
    abc170_c_1()
