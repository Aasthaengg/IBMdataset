def main():
    sx, sy, tx, ty = map(int, input().split())
    
    gapx = tx - sx
    gapy = ty - sy
    ans = ""

    #一回目tからsへ
    ans += "U" * gapy
    ans += "R" * gapx
    ans += "D" * gapy
    ans += "L" * gapx

    #二回目
    ans += "L"
    ans += "U" * (gapy + 1)
    ans += "R" * (gapx + 1)
    ans += "D"
    ans += "R"
    ans += "D" * (gapy + 1)
    ans += "L" * (gapx + 1)
    ans += "U"

    print(ans) 


if __name__ == "__main__":
    main()