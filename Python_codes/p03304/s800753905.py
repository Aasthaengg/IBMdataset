def solve():
    n,m,d = map(int,input().split())
    
    if d == 0:
        print((m-1) * (1/n))
    else:
        print((m-1) * ((2*n-2*d)/n**2))

if __name__ == '__main__':
    solve()