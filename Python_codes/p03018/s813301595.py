def main():
    import re
    s = input()
    s = s.replace('BC', 'D')

    obj = re.findall('[AD]+', s)
    ans = 0

    for x in obj:
        cnt = 0
        for i in x:
            if i == 'A':
                cnt += 1
            if i == 'D':
                ans += cnt

    print(ans)


if __name__ == '__main__':
    main()
