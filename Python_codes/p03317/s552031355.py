from sys import stdin
def main():
    #入力
    readline=stdin.readline
    N,K=map(int,readline().split())
    a=list(map(int,readline().split()))

    m=N-1
    l=K-1
    print((m+l-1)//l)
if __name__=="__main__":
    main()