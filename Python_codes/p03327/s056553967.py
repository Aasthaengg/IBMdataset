# A - ABD

# 1～999までは"ABC"、1000～1998までは"ABD"で始まるコンテスト名を返す


N = int(input())

if N <= 999:
    print('ABC')
elif N >= 1000 and N <= 1998:
    print('ABD')
