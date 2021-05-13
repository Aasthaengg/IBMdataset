from sys import stdin
def main():
    #入力
    readline=stdin.readline
    a,b,x=map(int,readline().split())

    if a==0:
        print(b//x+1)
    else:
        print(b//x-(a-1)//x)

if __name__=="__main__":
    main()