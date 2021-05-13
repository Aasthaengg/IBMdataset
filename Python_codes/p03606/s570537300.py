def resolve():
    record =[]
    for i in range(int(input())):
        l,r = map(int,input().split())
        record+=list(range(l,r+1))
    print(len(set(record)))

resolve()