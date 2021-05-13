from itertools import combinations_with_replacement 

N, M, Q = map(int, input().split())

Qset = []

for i in range(Q):
    a = list(map(int, input().split()))
    Qset.append(a)

ans = 0
for num in combinations_with_replacement(range(1, M+1), N):
    ans_temp = 0
    for j in Qset:
        if j[2] == num[j[1]-1] - num[j[0]-1]:
            ans_temp += j[3]

    ans = max(ans, ans_temp)

print(ans)