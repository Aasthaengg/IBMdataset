def resolve():
    N,K = map(int,input().split())
    if N%2 ==0:
        print("YES" if N//2 >= K else "NO")
    else:
        print("YES" if (N+1)//2 >=K else "NO")

    
resolve()