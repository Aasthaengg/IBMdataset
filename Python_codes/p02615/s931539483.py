def main():
    N=int(input())
    A=list(map(int,input().split()))

    A.sort(reverse=True)

    res=A[0]

    counter=1

    while counter<=N-2:
        index = (counter + 1) // 2
        res+=A[index]
        counter+=1

    print(res)

if __name__=="__main__":
    main()