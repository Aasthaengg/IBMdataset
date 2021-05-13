from sys import stdin
def main():
    #入力
    readline=stdin.readline
    a=int(readline())
    b=int(readline())
    h=int(readline())

    print((a+b)*h//2)
if __name__=="__main__":
    main()