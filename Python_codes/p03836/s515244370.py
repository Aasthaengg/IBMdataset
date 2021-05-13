def main():
    sx,sy,tx,ty=map(int, input().split())
    dx = tx-sx
    dy = ty-sy
    move = ""
    move+="U"*dy
    move+="R"*dx
    move+="D"*dy
    move+="L"*dx
    move+="D"
    move+="R"*(dx+1)
    move+="U"*(dy+1)
    move+="L"
    move+="U"
    move+="L"*(dx+1)
    move+="D"*(dy+1)
    move+="R"


    print(move)



if __name__ == '__main__':
    main()
