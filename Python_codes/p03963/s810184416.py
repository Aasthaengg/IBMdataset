s = input().split()

# ボールの数n
n = int(s[0])

# 色の種類k
k = int(s[1])

answer = 1

for num in range(n - 1):
    answer *= k - 1

answer *= k

print(int(answer))


