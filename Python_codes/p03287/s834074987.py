def main():
    import sys
    input = sys.stdin.readline
    from collections import Counter
    from itertools import accumulate

    n,m = map(int, input().split())
    a = [0] + list(map(lambda x: x % m, accumulate(map(int, input().split()))))
    c = Counter(a)
    res = 0
    for k, v in c.items():
            res += v*(v-1)//2
    print(res)
    
if __name__ == '__main__':
    main()
