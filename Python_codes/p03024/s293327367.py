def main():
    s = input().rstrip()
    cnt = 0
    for c in s:
        if c == "o":
            cnt += 1
    if cnt + (15-len(s)) >= 8:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()