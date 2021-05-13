def main():
    N,Y = map(int,input().split())
    for i in range(Y//10000+1):
        for j in range(N-i+1):
            if Y == i *10000 + j * 5000 + (N-i-j) * 1000:
                print(*[i,j,N-i-j])
                return
    print(*[-1,-1,-1])
main()