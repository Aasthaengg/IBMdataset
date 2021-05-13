N, M = map(int, input().split())
A_B = [list(map(int, input().split())) for _ in range(N)]

A_B.sort()
count = 0
money = 0
i = 0
while count != M:
    money += A_B[i][0] * min(M-count, A_B[i][1])
    count += min(M-count, A_B[i][1])
    i += 1
print(money)