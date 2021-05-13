def solve():
    n = int(input())
    p = list(map(int, input().split()))
    l = range(1,n+1)
    count = 0
    for i, j in zip(p, l):
        if i != j:
            count += 1
    print('YNEOS'[count>2::2])

if __name__ == '__main__':
    solve()
