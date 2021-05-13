# KEYENCE Programming Contest 2019 / キーエンス プログラミング コンテスト 2019: B – KEYENCE String
S = input()

is_keyence = 'NO'

for i in range(0, 8):
    if S[:i] + S[i - 7:] == 'keyence':
        is_keyence = 'YES'
        break

print(is_keyence)