def solve():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    c = 10000
    ci = 0
    for i, x in enumerate(h):
        tmp = abs(a - (t - x * 0.006))
        if c > tmp:
            c = tmp
            ci = i
    print(ci + 1)

if __name__ == '__main__':
    solve()
