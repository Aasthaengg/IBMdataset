import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    S = list(input())

    ans = 10 ** 6
    sum_count = S.count('E')
    for s in S:
        aft = 0
        if s == 'W':
            aft = 1
        else:
            sum_count -= 1
        ans = min(ans, sum_count)
        sum_count += aft
    print(ans)

if __name__ == '__main__':
    main()
