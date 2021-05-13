def main():
    from sys import stdin
    from collections import Counter
    readline = stdin.readline

    n = int(readline())
    S = [readline()[:-1] for _ in [0]*n]

    s = Counter(S)
    most = s.most_common(1)[0][1]

    answers = [i[0] for i in s.items() if i[1] == most]
    answers = sorted(answers)

    for ans in answers:
        print(ans)


if __name__ == '__main__':
    main()