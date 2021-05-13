def abc144c_walk_on_multiplication_table():
    def divisor(n):
        """ nの約数列挙 """
        ret = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                ret.append(i)
                if i ** 2 == n:
                    continue
                ret.append(n // i)
        return ret  # sortされていない
    ans = float('inf')
    n = int(input())
    a = divisor(n)
    for item in a:
        ans = min(ans, item-1+n//item-1)
    print(ans)
abc144c_walk_on_multiplication_table()