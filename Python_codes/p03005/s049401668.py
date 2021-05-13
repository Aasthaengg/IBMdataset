from sys import stdin

def solve(N, K):
    if K == 1:
        return 0
    else:
        return N - K


if __name__ == '__main__':
    N, K = [int(x) for x in stdin.readline().rstrip().split()]
    print(solve(N, K))
    
    # test
    # print(1 == solve(3,2))
    # print(0 == solve(3,1))
    # print(3 == solve(8,5))