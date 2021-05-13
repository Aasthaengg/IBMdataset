def resolve():
    s = input()

    ans = str()
    for char in s:
        if s.count(char) >1:
            ans = "no"
            break
        else:
            ans = "yes"
    print(ans)
resolve()