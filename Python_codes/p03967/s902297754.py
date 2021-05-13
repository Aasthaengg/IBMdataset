def main():
    s = input()
    ans = 0
    g_count = 0
    for c in s:
        if c == "g":
            if g_count:
                ans += 1
                g_count -= 1
            else:
                g_count += 1
        else:
            if g_count:
                g_count -= 1
            else:
                ans -= 1
                g_count += 1
    print(ans)

if __name__ == "__main__":
    main()