def solve():
    sx, sy, tx, ty = map(int, input().split())
    ans = ""
    ans += "R"*(tx-sx)+"U"*(ty-sy)
    ans += "L"*(tx-sx)+"D"*(ty-sy)
    ans += "D"+"R"*(tx-sx+1)+"U"*(ty-sy+1)+"L"
    ans += "U"+"L"*(tx-sx+1)+"D"*(ty-sy+1)+"R"
    print(ans)
    return 0

if __name__ == "__main__":
    solve()
