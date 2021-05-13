def solve():
    O = input()
    E = input()

    size = min(len(O), len(E))

    res = ""
    for i in range(size):
        res += O[i] + E[i]

    if len(O) > size:
        res += O[len(E):]
    elif len(E) > size:
        res += E[len(O):]

    return res


if __name__ == '__main__':
    res = solve()
    print(res)
