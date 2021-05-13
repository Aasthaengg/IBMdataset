def solve(s, t):
    dic1, dic2 = {}, {}
    for x, y in zip(s, t):
        if x in dic1:
            if dic1[x] != y:
                return False
        else:
            dic1[x] = y
        if y in dic2:
            if dic2[y] != x:
                return False
        else:
            dic2[y] = x
    return True


s = input()
t = input()

print('Yes' if solve(s, t) else 'No')