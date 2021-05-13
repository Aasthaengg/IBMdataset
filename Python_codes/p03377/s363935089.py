cat, unknown, guess = map(int, input().split())
if guess > cat:
    if cat + unknown < guess:
        print('NO')
    else:
        print('YES')
else:
    if guess + unknown > cat + unknown:
        print('NO')
    else:
        if cat > guess:
            print('NO')
        else:
            print('YES')