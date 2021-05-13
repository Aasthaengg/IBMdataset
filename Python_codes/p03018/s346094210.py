def main():
    s = list(input().rstrip())
    ans = 0
    cnt = 0
    for i in range(len(s)-2):
        if s[i] == "A":
            cnt += 1
        else:
            cnt = 0
        if s[i] == "A" and s[i+1] == "B" and s[i+2] == "C":
            ans += cnt
            if cnt == 1:
                s[i+2] = "A"
                cnt = 0
            else:
                s[i+1] = "A"
                s[i+2] = "A"
                cnt -= 2
    print(ans)

if __name__ == "__main__":
    main()