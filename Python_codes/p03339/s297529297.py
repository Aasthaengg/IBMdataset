from sys import stdin
def main():
    #入力
    readline=stdin.readline
    N=int(readline())
    S=readline().strip()

    t_left=0
    t_right=N-1
    left=0
    right=0
    for i in range(1,N):
        if S[i]=="W":
            right+=1

    res=0
    min_res=N
    for i in range(N):
        res=abs(t_left-left)+abs(t_right-right)
        min_res=min(min_res,res)
        if i!=N-1:
            t_left+=1
            t_right-=1
            if S[i]=="E":
                left+=1
            if S[i+1]=="W":
                right-=1

    print(min_res)
if __name__=="__main__":
    main()