# C - Colorful Leaderboard
def main():
    _ = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    ans = []

    for i in a:
        if i // 400 >= 8:
            cnt += 1
        else:
            ans.append(i//400)
    else:
        ans = set(ans)
        print(max(len(ans), 1), len(ans)+cnt)



if __name__ ==  "__main__":
    main()