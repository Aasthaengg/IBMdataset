N = int(input())
AB = [list(map(int,input().split())) for _ in range(N)]

scores = [(A+B, A, B) for A,B in AB]
scores.sort(key=lambda x:x[0], reverse=True)
takahashi = 0
aoki = 0
takahashi_turn = True
for score in scores:
    if takahashi_turn:
        takahashi += score[1]
    else:
        aoki += score[2]
    takahashi_turn = not takahashi_turn
print(takahashi-aoki)