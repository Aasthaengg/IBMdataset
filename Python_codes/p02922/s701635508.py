"""
A:プラグの数
B:必要なプラグの数
"""

A, B = map(int, input().split())
count = 0

if B == 1:
    print(0)
elif A >= B:
    print(1)
else:
    while True:
        B -= (A - 1)
        count += 1
        if B <= A:
            count += 1
            break

    print(count)
