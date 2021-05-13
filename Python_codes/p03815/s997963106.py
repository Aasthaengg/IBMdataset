def c_yet_another_die_game():
    X = int(input())
    q, r = divmod(X, 11)
    return 2 * q + ((r - 1) // 6 + 1)

print(c_yet_another_die_game())