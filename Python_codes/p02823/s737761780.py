# AtCoder Grand Contest 041
# A - Table Tennis Training

def f(A,B,n) :
    judge=B-A

    if judge%2==0 :
        n+=judge//2
        return(n)

    else :
        if abs(A-1) < abs(N-B) :
            if A==1 :
                A=A
                B-=1
                n+=1
            else:
                B-=A-1
                n+=A-1
                A-=A-1
            return f(A,B,n)
        else :
            if B==N :
                B=B
                A+=1
                n+=1
            else :
                A+=abs(N-B)
                n+=abs(N-B)
                B+=abs(N-B)
            return f(A,B,n)

N,A,B=map(int,input().split())
print(f(A,B,0))