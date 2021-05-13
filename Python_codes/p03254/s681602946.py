def resolve():
    N,x = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    Acouont = 0
    ans = 0
    if sum(A) < x:
        print(N-1)
    else:
        for i in range(N):
            Acouont = Acouont + A[i]
            #print (Acouont)
            if Acouont > x:
                break
            ans += 1
        print(ans)   
resolve()