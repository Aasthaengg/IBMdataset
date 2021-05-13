def resolve():
    s = input()
    a = s.find("a")
    b = s.find("b")
    c = s.find("c")
    if a != -1 and b != -1 and c != -1:
        print("Yes")
    else:
        print("No")
resolve()