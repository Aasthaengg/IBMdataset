from sys import stdin
def main():
    #入力
    readline=stdin.readline
    N,A,B=map(int,readline().split())
    if (B-A)%2==0:
        print((B-A)//2)
    else:
        print(min(N-B,A-1)+1+(B-A-1)//2)

if __name__=="__main__":
    main()