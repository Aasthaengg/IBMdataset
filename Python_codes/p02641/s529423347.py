def abc170_c():
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

if __name__ == '__main__':
    abc170_c()