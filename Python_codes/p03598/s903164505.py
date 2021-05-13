def resolve():
    '''
    code here
    '''
    N = int(input())
    K = int(input())
    xs = [int(item) for item in input().split()]

    res = 0
    for i in range(N):
        res += min(xs[i]*2, (K-xs[i])*2)

    print(res)

if __name__ == "__main__":
    resolve()
