import copy


def resolve(L_input):
    L = copy.deepcopy(L_input)
    cnt = 0
    s = L[0]
    for i in range(1, len(L)):
        a = L[i]
        if s > 0 and s+a >= 0:
            L[i] = -s-1
            cnt += (s+a+1)
            s = -1
        elif s < 0 and s+a <= 0:
            L[i] = -s+1
            cnt += (-s-a+1)
            s = 1
        else:
            s += a

    return cnt


def solution(L):
    first_term = L[0]
    if first_term > 0:
        L_positive = L
        first_positibe_cnt = resolve(L_positive)
        # extract first_term+1 to first_term to be -1
        L_negative = [-1]+L[1:]
        first_negative_cnt = (first_term+1) + resolve(L_negative)
    elif first_term < 0:
        # add -first_term+1 to first_term to be 1
        L_positive = [1]+L[1:]
        first_positibe_cnt = (-first_term+1) + resolve(L_positive)
        L_negative = L
        first_negative_cnt = resolve(L_negative)
    else:
        # add 1 to first_term to be 1
        L_positive = [1]+L[1:]
        first_positibe_cnt = 1 + resolve(L_positive)
        # extract 1 to first_term to be -1
        L_negative = [-1]+L[1:]
        first_negative_cnt = 1 + resolve(L_negative)

    # print("first_positive, cnt: {}".format(first_positibe_cnt))
    # print(L_positive)
    # print("first_negative_cnt, cnt: {}".format(first_negative_cnt))
    # print(L_negative)

    return min(first_positibe_cnt, first_negative_cnt)


if __name__ == "__main__":
    N = int(input())
    L = list(map(int, input().split(' ')))
    print(solution(L))
