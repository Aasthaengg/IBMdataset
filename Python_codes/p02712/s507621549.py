n = int(input())


def souwa(n):
    syo, jyoyo = divmod(n, 2)
    return (n + 1) * syo + (n + 1) // 2 * jyoyo


print(souwa(n) - souwa(n//3)*3 - souwa(n//5)*5 + souwa(n//15)*15)