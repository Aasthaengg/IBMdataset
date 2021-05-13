def main():
    N, K = map(int, input().split())

    if K == 0:
        return N * N

    count = 0
    for b in range(K+1, N+1):
        count += (N-K+1)//b * (b-K) + min(b-K, (N-K+1) % b)
    return count

if __name__ == '__main__':
    print(main())
