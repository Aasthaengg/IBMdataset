def resolve():
    l=list(map(int, input().split()))
    l.sort(reverse=True)
    if l[0]==l[1]+l[2]:
        print('Yes')
    else:
        print('No')
resolve()