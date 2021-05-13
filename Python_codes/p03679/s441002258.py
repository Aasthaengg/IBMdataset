def actual(X, A, B):
    is_unexpired = (A - B)

    if is_unexpired >= 0:
        return 'delicious'

    elapsed_after_expiration_day = (B - A)
    if elapsed_after_expiration_day <= X:
        return 'safe'

    return 'dangerous'

X, A, B = map(int, input().split())
print(actual(X, A, B))