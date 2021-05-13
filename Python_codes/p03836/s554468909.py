from sys import stdin
def main():
    #入力
    readline=stdin.readline
    sx,sy,tx,ty=map(int,readline().split())

    ans=""
    u=ty-sy
    v=tx-sx
    a=u*"U"
    b=v*"R"
    c=u*"D"
    d=v*"L"
    ans+=a+b+c+d
    ans+="L"+a+"U"+b+"R"+"D"
    ans+="R"+c+"D"+d+"L"+"U"
    print(ans)

if __name__=="__main__":
    main()