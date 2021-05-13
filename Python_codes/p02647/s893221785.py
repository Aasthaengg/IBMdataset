def main():
    N,K=map(int,input().split())
    A=list(map(int,input().split()))


    for _ in range(K):
        counter=[0 for _ in range(N)]

        for i in range(len(A)):
            left=max(0,i-A[i])
            right=min(N-1,i+A[i])
            counter[left]+=1
            if right+1<N:
                counter[right+1]-=1
        for i in range(len(counter)-1):
            counter[i+1]+=counter[i]

        if counter==A:
            break
        else:
            A=counter

    for i in range(N):
        if i!=N-1:
            print(str(A[i])+" ",end="")
        else:
            print(A[i])

if __name__ == "__main__":
    main()
