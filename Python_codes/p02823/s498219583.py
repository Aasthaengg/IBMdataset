def main():
    N,A,B=map(int,input().split())
    if (B-A)%2:
        print((B-A)//2 + 1 + min(N-B,A-1))
    else:
        print((B-A)//2)

main()