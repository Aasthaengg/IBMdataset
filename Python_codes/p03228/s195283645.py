def exc(cookies, turn):
    exccs = 0
    subturn = (turn + 1) % 2
    if (cookies[turn] % 2) == 0:
        exccs = cookies[turn] //2
    else:
        exccs = (cookies[turn] - 1) // 2
    
    cookies[subturn] += exccs
    cookies[turn] = exccs

    return cookies

a, b, k = map(int, input().split())
cookies = [a, b]

for i in range(k):
    turn = i % 2
    cookies = exc(cookies, turn)

print("{} {}".format(cookies[0], cookies[1]))