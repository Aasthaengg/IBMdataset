# Battle
A, B, C, D = map(int, input().split())
HP = [A, C]
Attack = [B, D]
Turn = False
while (HP[0] > 0) & (HP[1] > 0):
    HP[not Turn] -= Attack[Turn]
    Turn = not Turn
print(['No', 'Yes'][Turn])