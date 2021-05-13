def solve():
    D,T,S = map(int,input().split())
    if T < D / S:
        print('No')
    else:
        print('Yes')
if __name__ == '__main__':
    solve()
