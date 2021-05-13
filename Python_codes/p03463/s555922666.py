def a_move_and_win(N, A, B):
    ans = 'Alice' if (B - A + 1) % 2 == 1 else 'Borys'
    return ans

N, A, B = [int(i) for i in input().split()]
print(a_move_and_win(N, A, B))