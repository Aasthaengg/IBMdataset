def main():

    N = int(input())
    S = []
    pos = []
    neg1 = []
    neg2 = []
    tot_v = 0
    for _ in range(N):
        t = input()
        S.append(t)
        v = 0
        min_v = float('inf')
        for c in t:
            if c == '(': v += 1
            else: v -= 1
            min_v = min(min_v, v)
        tot_v += v
        if min_v >=0:
            pos.append([min_v, v])
        else:
            if v > 0:
                neg1.append([min_v, v])
            else:
                neg2.append([min_v-v, min_v, v])

    if tot_v !=  0: return "No"

    u = 0
    for _, v in pos:
        u += v

    neg1.sort(reverse = True, key = lambda x: x[0])
    for min_v, v in neg1:
        if u + min_v < 0:
            return "No"
        else:
            u += v


    neg2.sort(key = lambda x: x[0])
    for _, min_v, v in neg2:
        if u + min_v < 0:
            return "No"
        else:
            u += v

    return "Yes"


if __name__ == '__main__':
    print(main())