def resolve():
    A,B,N = map(int,input().split())
    x = min(N,B-1)
    ans = int(A * x / B) 
    print(ans)
resolve()