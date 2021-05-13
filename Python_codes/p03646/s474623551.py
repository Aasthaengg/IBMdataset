from sys import stdin
def main():
    #入力
    readline=stdin.readline
    K=int(readline())

    N=50
    M=K//N
    L=K%N
    A=range(N)
    A=list(map(lambda x:x+M,A))
    for i in range(L):
        A[i]+=N+1
        A=list(map(lambda x:x-1,A))

    print(N)
    print(*A)

if __name__=="__main__":
    main()