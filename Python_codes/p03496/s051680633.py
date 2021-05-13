def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    ans = list()
    # to same signs
    max_A, min_A = max(A), min(A)
    all_positive = (min(A) > 0)
    if max_A >= 0 >= min_A:
        if max_A > abs(min_A):
            max_index = A.index(max_A)
            for i in range(N):
                if i == max_index:
                    continue
                ans.append('{} {}'.format(max_index + 1, i + 1))
            all_positive = True
        else:
            min_index = A.index(min_A)
            for i in range(N):
                if i == min_index:
                    continue
                ans.append('{} {}'.format(min_index + 1, i + 1))
            all_positive = False
    # cumulative sum
    if all_positive:
        for i in range(N - 1):
            ans.append('{} {}'.format(i + 1, i + 2))
    else:
        for i in range(N - 1):
            ans.append('{} {}'.format(N - i, N - i - 1))
    print(len(ans))
    for a in ans:
        print(a)


if __name__ == '__main__':
    main()