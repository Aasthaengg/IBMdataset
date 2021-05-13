def resolve():
    n,k=map(int, input().split())
    l=list(map(int, input().split()))
    l.sort(reverse=True)
    l_new=l[:k]
    print(sum(l_new))
resolve()