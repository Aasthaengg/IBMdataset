# KEYENCE Programming Contest 2019 / キーエンス プログラミング コンテスト 2019: A – Beginning
n = input().split()
n.sort()
print('YES' if n[0] + n[1] + n[2] + n[3] == '1479' else 'NO')