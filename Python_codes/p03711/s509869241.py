def resolve():
    x, y = map(int, input().split())

    g1 = [1, 3, 5, 7, 8, 10, 12]
    g2 = [4, 6, 9, 11]
    g3 = 2

    ans = str()
    if x in g1 and y in g1:
        ans = "Yes"
    elif x in g2 and y in g2:
        ans = "Yes"
    elif x == g3 and y == g3:
        ans = "Yes"
    else:
        ans = "No"
    print(ans)
resolve()