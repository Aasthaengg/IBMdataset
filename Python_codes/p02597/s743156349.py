def main():
    _ = int(input())
    S = input()
    ri = S.count("R")  # 右側の換えるべき個数
    le = 0
    ans = max(ri, le)
    for s in S:
        if s == "R":
            ri -= 1
        else:
            le += 1
        ans = min(ans, max(ri, le))
    print(ans)


if __name__ == '__main__':
    main()
