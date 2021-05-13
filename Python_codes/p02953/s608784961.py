def solve():
    N = int(input())
    H = [int(i) for i in input().split()]
    if N == 1:
        print('Yes')
    elif N == 2:
        print('Yes' if abs(H[0] - H[1]) <= 1 else 'No')
    else:
        for i in range(1, N)[::-1]:
            l = H[i - 1]
            r = H[i]
            if l <= r:
                continue
            elif l - 1 <= r:
                H[i - 1] -= 1
            else:
                print('No')
                exit()
        print('Yes')

if __name__ == "__main__":
    solve()