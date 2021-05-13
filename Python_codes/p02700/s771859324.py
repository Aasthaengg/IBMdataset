A,B,C,D = map(int,input().split())

Takahashi_HP = A
Takahashi_Damage = B
Aoki_HP = C
Aoki_Damage = D

while Takahashi_HP > 0 or  Aoki_HP > C:
    Aoki_HP -= Takahashi_Damage
    if Aoki_HP <= 0:
        print('Yes')
        break
    Takahashi_HP -= Aoki_Damage
    if Takahashi_HP <= 0:   
        print('No')
        break