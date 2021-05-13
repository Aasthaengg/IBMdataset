a_poll, b_poll, c_poll = map(int, input().split())

if b_poll - a_poll == c_poll - b_poll:
    print('YES')
else:
    print('NO')