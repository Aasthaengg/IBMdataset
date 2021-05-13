from sys import stdin
def main():
    #入力
    readline=stdin.readline
    N=int(readline())
    F=[]
    for i in range(N):
        f=list(map(int,readline().split()))
        F.append(f)
    P=[]
    for i in range(N):
        p=list(map(int,readline().split()))
        P.append(p)
    
    max_res=-float("inf")
    for i in range(1<<10):
        if i==0:
            continue
        else:
            output=[]
            for j in range(10):
                if(i>>j)&1:
                    output.append(j)

            oc=[0]*10  #open or close
            for j in output:
                oc[j]=1
            
            res=0
            for j in range(N):
                c=0
                for k in range(10):
                    if oc[k]==1 and F[j][k]==1:
                        c+=1
                res+=P[j][c]
            max_res=max(res,max_res)

    print(max_res)
    
if __name__=="__main__":
    main()