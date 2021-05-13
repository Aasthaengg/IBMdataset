def resolve():
    n = int(input())
    cl = list(map(str, input().split()))
    isY = False
    for i in cl:
        if i == "Y":
            isY = True
    if isY:
        print("Four")
    else:
        print("Three")
resolve()