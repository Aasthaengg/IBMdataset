def solve():
    O = input()
    E = input()

    size = min(len(O), len(E))

    lis = []
    for i in range(size):
        lis.append(O[i] + E[i])

    if len(O) > size:
        lis.append(O[len(E):])
    elif len(E) > size:
        lis.append(E[len(O):])

    return "".join(lis)


if __name__ == '__main__':
    res = solve()
    print(res)
