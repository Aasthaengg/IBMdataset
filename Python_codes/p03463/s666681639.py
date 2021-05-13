from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n,a,b=map(int,readline().split())
    print("Alice" if (b-a)%2==0 else "Borys")

if __name__=="__main__":
    main()