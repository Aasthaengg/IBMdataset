D = int(input())
C = list(map(int, input().split()))
S = []
for i in range(D):
    S.append(list(map(int, input().split())))

T = []
for i in range(D):
    T.append(int(input()))

distance_list = [0] * 26

sum_ = 0
for i in range(D):
    sum_ += S[i][T[i]-1]
    down = 0
    for j in range(26):
        if T[i] - 1 == j:
            distance_list[j] = 0
            continue
        distance_list[j] += 1
        down += distance_list[j] * C[j]
    sum_ -= down

    print(sum_)
