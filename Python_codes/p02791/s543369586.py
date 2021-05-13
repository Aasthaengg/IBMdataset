def main():

    N = int(input())
    P = list(map(int, input().split()))

    ans = 0
    min_v = float('inf')
    for i in range(N):
        if P[i] <= min_v:
            min_v = P[i]
            ans += 1
    return ans

if __name__ == '__main__':
    print(main())
