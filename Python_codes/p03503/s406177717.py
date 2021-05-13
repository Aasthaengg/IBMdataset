from sys import stdin
def main():
    #入力
    readline=stdin.readline
    N=int(readline())
    F=[]
    for i in range(N):
        f=int("".join(readline().strip().split(" ")),2)
        F.append(f)
    P=[]
    for i in range(N):
        p=list(map(int,readline().split()))
        P.append(p)
    
    max_res=float("-inf")
    for output in range(1,1<<10):
        res=0
        for j in range(N):
            c=bin(output&F[j]).count("1")
            res+=P[j][c]
        max_res=max(res,max_res)

    print(max_res)
    
if __name__=="__main__":
    main()