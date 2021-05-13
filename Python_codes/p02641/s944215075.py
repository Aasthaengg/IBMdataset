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

        ans = min(search_values, key=lambda a: abs(a - x))

        return ans
    
    print(solve())

if __name__ == '__main__':
    abc170_c_1()
