def resolve():
    n,k=map(int, input().split())
    sum=0
    for i in range(k):
        sum+=(n-i)//k
    print(sum)
resolve()