def main():
    N = int(input())
    a = [None] + list(map(int, input().split()))
    b = [None] + [0]*N
    for i in range(N, 0, -1):
        ball = [b[j] for j in range(i, N+1, i)]
        if sum(ball) % 2 != a[i]:
            b[i] = 1
    ans = [str(i) for i, n in enumerate(b) if n==1]
    print(len(ans))
    print(' '.join(map(str, ans)))
main()