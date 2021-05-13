if __name__ == '__main__':
    N = int(input())

    if N == 0:
        print(0)
        exit()

    ans = []
    cnt = 0
    while abs(N) >= 1:
        mod_val = N % ((-2) ** (cnt + 1))
        if mod_val == 0:
            ans.append(0)
        else:
            ans.append(1)
            N -= (-2) ** cnt
        cnt += 1

    print(''.join([str(val) for val in ans[::-1]]))
