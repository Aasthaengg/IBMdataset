from sys import stdin
def main():
    #入力
    readline=stdin.readline
    N=int(readline())
    A=list(map(int,readline().split()))

    res=0
    for i in range(N):
        res+=A[i]-1
    
    print(res)
if __name__=="__main__":
    main()