def main():
    n = int(input())
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))

    scores = []
    for i1 in range(n):
        score = sum(a1[:i1+1]) + sum(a2[i1:])
        scores.append(score)
    r = max(scores)
    print(r)


if __name__ == '__main__':
    main()
