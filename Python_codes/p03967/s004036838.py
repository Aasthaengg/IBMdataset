if __name__ == "__main__":
    s = input()

    ans = 0
    g_count = 0
    p_count = 0
    for i in range(len(s)):
        if g_count >= p_count + 1 and s[i] is 'g':
            p_count += 1
            ans += 1
        elif s[i] is 'g':
            g_count += 1
        elif g_count >= p_count + 1 and s[i] is 'p':
            p_count += 1
        else:
            g_count += 1
            ans -= 1

    print(ans)
