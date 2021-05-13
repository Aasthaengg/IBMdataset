def resolve():
    x, y = map(int, input().split())
    list = [1, 3, 5, 7, 8, 10, 12]
    lists = [4, 6, 9, 11]
    print("Yes" if (list.count(x) == 1 and list.count(y)) or (lists.count(x) == 1 and lists.count(y)) else "No")
resolve()