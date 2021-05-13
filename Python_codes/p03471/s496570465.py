def main():
    N, Y = map(int, input().split())
    m = 10000
    ft = 5000
    t = 1000
    for i in range(N+1):
        for j in range(N-i+1):
            k = N - i - j
            if m*i + ft*j + t*k == Y and i + j + k == N:
                print(str(i) + ' ' + str(j) + ' ' + str(k))
                return
    print('-1 -1 -1')

main()  