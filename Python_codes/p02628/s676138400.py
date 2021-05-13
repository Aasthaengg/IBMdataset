from sys import stdin
input = stdin.readline

MOD = 10**9 + 7





def solve():
    N,K = map(int,input().split())
    p = list(map(int,input().split()))
    p.sort()
    print(sum(p[:K]))




if __name__ == '__main__':
    solve()
