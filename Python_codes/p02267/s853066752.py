def main():
    N = int(input())
    S = set(map(int, input().split()))
    Q = int(input())
    T = set(map(int, input().split()))

    cnt = 0
    for i in T:
        if i in S:
            cnt += 1

    print(cnt)

main()