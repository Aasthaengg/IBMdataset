def p_f_2():
    n, m = map(int, input().split())
    *s, = map(int, input())
    s.reverse()
    i = 0
    ans = []
    while i + m < n:
        for j in reversed(range(i + 1, i + m + 1)):
            if s[j] == 0:
                ans.append(j - i)
                i = j
                break
        else:
            print(-1)
            exit()
    ans.append(n-i)
    print(*reversed(ans))

if __name__ == '__main__':
    p_f_2()
