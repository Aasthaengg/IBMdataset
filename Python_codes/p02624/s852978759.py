# from sys import stdin
# input = stdin.readline


def solve():
    N = int(input())
    res = 0
    for i in range(1,N+1):
        k = N // i
        res +=i*(k+1)*k//2
    print(res)







if __name__ == '__main__':
    solve()