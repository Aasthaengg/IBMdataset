N = int(input())
A = list(map(int, input().split()))

odd = 0  # 奇数
even = 0  # 偶数
for ai in A:
    if ai % 2 == 0:
        odd += 1
    else:
        even += 1

if even % 2 == 0:
    print('YES')
else:
    print('NO')