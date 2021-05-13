def main():
    N, K = map(int, input().split())
    l = list(map(int, input().split()))
    a = 0
    for i in range(N):
        if l[i] >= K:
            a = a + 1
    print(a)
main()