def main(S, T):
    score = float('inf')
    org_length = len(S)
    part_length = len(T)

    for i in range(0, org_length - part_length + 1):
        part_str = S[i:i + part_length]

        count = 0
        for a, b in zip(part_str, T):
            if a != b:
                count+=1
        score = min(count, score)

    print(score)


if __name__ == '__main__':
    S = input()
    T = input()
    main(S, T)
