def main():
    s = input()
    t = input()

    len_s, len_t = len(s), len(t)
    num_iter = len_s - len_t + 1
    answer = len_t
    for i in range(num_iter):
        s_sub = s[i : i+len_t]
        count = 0
        for s_i, t_i in zip(s_sub, t):
            if s_i == t_i:
                count += 1
        answer = min(answer, len_t-count)
    print(answer)


if __name__ == '__main__':
    main()
