A, B, C, D = map(int, input().split())
takahashi_turn = True
while A > 0 and C > 0:
    if takahashi_turn:
        C -= B
    else:
        A -= D
    takahashi_turn = not takahashi_turn
print('No' if A <= 0 else 'Yes')