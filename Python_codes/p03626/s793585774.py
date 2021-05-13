n = int(input())

s1 = input()
s2 = input()

INF = 1000000007

left = None
index = 0
cnt = 0
while index < n:
    # 右側が縦テトリス1つ
    if s1[index] == s2[index]:
        index += 1
        if left is None:
            left = 1
            cnt = 3
        # 左側が縦テトリス1つ
        elif left == 1:
            cnt *= 2
        # 左側が横テトリス2つ
        else:
            cnt *= 1
        left = 1

    # 右側が横テトリス2つ
    else:
        index += 2
        if left is None:
            left = 2
            cnt = 6
        # 左側が縦テトリス1つ
        elif left == 1:
            cnt *= 2
        # 左側が横テトリス2つ
        else:
            cnt *= 3
        left = 2
    cnt = cnt % INF
print(cnt)