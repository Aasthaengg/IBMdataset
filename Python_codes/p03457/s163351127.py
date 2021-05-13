def main():
    n = int(input())
    txys = [list(map(int, input().split())) for _ in range(n)]
    txys.insert(0, [0, 0, 0])
    ans = 'Yes'
    for i in range(n):
        time_diff = txys[i+1][0] - txys[i][0]
        manhattan_dis = abs(txys[i][1] - txys[i+1][1]) + abs(txys[i][2] - txys[i+1][2])
        if time_diff < manhattan_dis:
            ans = 'No'
            break
        elif time_diff == manhattan_dis:
            continue
        else:
            if (time_diff - manhattan_dis) % 2 == 0:
                continue
            else:
                ans = 'No'
                break
    print(ans)


if __name__ == "__main__":
    main()
