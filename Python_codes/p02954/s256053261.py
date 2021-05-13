import copy


def move(C, S):
    newC = copy.copy(C)
    for i, s in enumerate(S):
        if s == "L":
            newC[i - 1] += C[i]
        else:
            newC[i + 1] += C[i]
        newC[i] -= C[i]
        # print(C, newC)
    return newC


def main():
    S = input()
    N = len(S)
    C = [0] * N

    odd_cnt, even_cnt = 0, 0
    for i, s in enumerate(S):
        if s == 'R':
            if (i + 1) % 2 == 0:
                even_cnt += 1
            else:
                odd_cnt += 1
        else:
            if (i + 1) % 2 == 0:
                C[i] += even_cnt
                C[i - 1] += odd_cnt
                odd_cnt, even_cnt = 0, 0
            else:
                C[i] += odd_cnt
                C[i - 1] += even_cnt
                odd_cnt, even_cnt = 0, 0
        # print(i, S, odd_cnt, even_cnt, C)

    C = list(reversed(C))
    odd_cnt, even_cnt = 0, 0
    for i, s in enumerate(reversed(S)):
        if s == 'L':
            if (i + 1) % 2 == 0:
                even_cnt += 1
            else:
                odd_cnt += 1
        else:
            if (i + 1) % 2 == 0:
                C[i] += even_cnt
                C[i - 1] += odd_cnt
                odd_cnt, even_cnt = 0, 0
            else:
                C[i] += odd_cnt
                C[i - 1] += even_cnt
                odd_cnt, even_cnt = 0, 0
        # print(i, ''.join(list(reversed(S))), odd_cnt, even_cnt,
        #       list(reversed(C)))

    C = reversed(C)
    print(' '.join([str(c) for c in C]))


if __name__ == "__main__":
    main()