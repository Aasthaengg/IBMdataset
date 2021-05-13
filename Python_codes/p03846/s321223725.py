
def mod_(b, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res * b % mod
        b = b * b % mod
        n >>= 1
    return int(res)

def main():

    N = int(input())
    A = list(map(int, input().split()))

    n = ((N+1) >> 1)
    li = [0]*n



    for a in A:
        li[a >> 1] += 1

    if N & 1:
        if li[0] != 1:
            print(0)
        elif li.count(2) != n-1:
            print(0)
        else:
            c = n-1
            print(2 ** c % (10**9+7))
    else:
        if li.count(2) != n:
            print(0)
        else:
            c = n
            print(2 ** c % (10**9+7))

main()