def main():
    import math
    from functools import reduce
    def gcd_list(l):
        return reduce(math.gcd, l)
    n, k = list(map(int, input().split()))
    A = list(map(int, input().split()))
    g = gcd_list(A)
    m = max(A)
    if k % g == 0 and k <= m:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')

if __name__ == '__main__':
    main()
