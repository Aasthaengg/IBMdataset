

def solve(M,K):
    if K>=2**M:
        return False
    if M==0:
        if K==0:
            return ["0","0"]
        else:
            return False
    elif M==1:
        if K==1:
            return False
        else:
            return ["0","0","1","1"]
    else:
        b=list(range(2**M))
        b.remove(K)
        import copy
        c=copy.deepcopy(b)
        c.reverse()
        return b+[K]+c+[K]

if __name__ == '__main__':
    M,K=list(map(int,input().split()))
    ans=solve(M,K)
    if ans is False:
        print(-1)
    else:
        for i in range(len(ans)):
            if i!=len(ans):
                print("{} ".format(ans[i]),end="")
            else:
                print(ans[i])