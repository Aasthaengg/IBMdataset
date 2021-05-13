def main():
    sx,sy,tx,ty=map(int,input().split())
    s=(sx,sy)
    t=(tx,ty)
    dif_y = abs(ty-sy)
    dif_x = abs(tx-sx)
    ans = "U"*dif_y+"R"*dif_x
    ans += "D"*dif_y+"L"*dif_x
    ans += "L"+"U"*(dif_y+1)+"R"*(dif_x+1)+"D"
    ans += "R"+"D"*(dif_y+1)+"L"*(dif_x+1)+"U"
    print(ans)

if __name__ == "__main__":
    main()