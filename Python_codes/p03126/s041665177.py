def main():
    N, M = map(int, input().split())
    K = []
    for i in range(N):
        K.append(list(map(int, input().split())))
    l = []
    ans = 0
    for i in range(M+1):
        l.append(0)
    for i in range(N):
        for j in range(K[i][0]):
            l[K[i][j+1]] += 1
    for i in range(len(l)):
        if l[i] == N:
            ans += 1
    print(ans)
main()