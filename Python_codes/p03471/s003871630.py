def main():
    N,Y=map(int,input().split())
    for i in range(N+1):
        for j in range(0,N-i+1):
            k=N-i-j
            if i*10000+j*5000+k*1000==Y:
                print(i,end=" ")
                print(j,end=" ")
                print(k)
                return 0
    print("-1 -1 -1")
main()