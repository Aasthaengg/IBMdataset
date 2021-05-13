def aa098():
    a,b = list(map(int, input().split()))
    c = [a+b, a-b, a*b]
    print(max(c))

aa098()
