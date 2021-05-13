def solve():
    N = int(input())
    A = list(map(int, input().split()))

    four_cnt = 0
    two_cnt = 0
    buta = 0
    for a in A:
        if a % 4 == 0:
            four_cnt += 1
        elif a % 2 == 0:
            two_cnt += 1
        else:
            buta += 1
    
    if two_cnt > 0:
        if buta <= four_cnt:
            print('Yes')
        else:
            print('No')
    else:
        if buta <= four_cnt + 1:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    solve()