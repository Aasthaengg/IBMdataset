S = list(input())

cnt = [0]*len(S)

cnt_B = 0
for i,j in enumerate(S):
    if j == 'B':
        cnt_B += 1
    if j == 'W':
        cnt[i] = cnt_B
print(sum(cnt))