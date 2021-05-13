def main():
    s = input()
    s_l = len(s)
    cnt = 0
    for i in range(s_l//2):
        if s[i] != s[::-1][i]:
        # if s[i] != s[s_l-i-1]:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()