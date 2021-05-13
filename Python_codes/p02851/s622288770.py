def main():
    from itertools import accumulate
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    A=list(accumulate(A))
    A=[[(A[i]-i-1)%K,i+1] for i in range(0,N)]
    A.append([0,0])
    A.sort()
    s=1
    start=0
    count=0
    for i in range(0,N):
        if A[i][0]==A[i+1][0]:
            s+=1
        else:
            X=[A[i][1] for i in range(start,start+s)]
            a=0
            b=0
            subcount=0
            while len(X)-1>=a and len(X)-1>=b:
                if K-1>=X[b]-X[a]:
                    b+=1
                else:
                    subcount+=len(X)-b
                    a+=1
            count+=len(X)*(len(X)-1)//2-subcount
            start+=s
            s=1
    X=[A[i][1] for i in range(start,start+s)]
    a=0
    b=0
    subcount=0
    while len(X)-1>=a and len(X)-1>=b:
        if K-1>=X[b]-X[a]:
            b+=1
        else:
            subcount+=len(X)-b
            a+=1
    count+=len(X)*(len(X)-1)//2-subcount
    print(count)

if __name__ == '__main__':
    main()
