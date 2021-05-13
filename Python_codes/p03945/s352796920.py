# C - 一次元リバーシ
def main():
    s = input()
    t = s[0]
    cnt = 1

    for i in range(1, len(s)):
        if t != s[i]:
            t = s[i]
            cnt += 1
    else:
        print(cnt-1)
            

if __name__ ==  "__main__":
    main()