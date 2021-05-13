def solve():
    n = 5
    x = [int(input()) for _ in range(n)]
    k = int(input())
    for i in range(n):
        for j in range(i+1, n):
            if x[j] - x[i] > k:
                print(':(')
                exit()
    print('Yay!')


if __name__ == '__main__':
    solve()
