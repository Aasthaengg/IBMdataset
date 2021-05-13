from sys import stdin

input = stdin.readline

MOD = 10**9 + 7



def solve():
    n = int(input())
    print((pow(10,n,MOD) - pow(9,n,MOD) * 2 + pow(8,n,MOD))%MOD)

if __name__ == '__main__':
    solve()
