def main():
    N, T = list(map(int, input().split(' ')))
    A = list(map(int, input().split(' ')))
    score_list = [0 for _ in range(N)]
    min_price = A[0]
    for i in range(N):
        a = A[i]
        score_list[i] = a - min_price
        min_price = min(a, min_price)
    max_score = max(score_list)
    ans = 0
    for i in range(N):
        if score_list[i] == max_score:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()