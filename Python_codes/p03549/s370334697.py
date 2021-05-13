from sys import stdin
def main():
    #入力
    readline=stdin.readline
    N,M=map(int,readline().split())

    a=M*1900+(N-M)*100
    down=2**M

    print(a*down)

if __name__=="__main__":
    main()