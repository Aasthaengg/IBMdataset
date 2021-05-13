def resolve():
    N=int(input())
    s=str(N)
    val=0
    for i in s:
        val+=int(i)
    print(10 if N in [10, 100, 1000,1000,10000,100000] else val)
    


resolve()