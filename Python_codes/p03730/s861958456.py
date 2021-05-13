def solve():
    A,B,C = map(int,input().split())
    for n in range(10**6):
        if n * A % B == C:
            print('YES')
            return
    
    else:
        print('NO')

if __name__ == '__main__':
    solve()