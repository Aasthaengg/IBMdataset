import copy

N = input()
S = list(map(int, input()[:]))
left = [False for i in range(10)]
right = [0 for i in range(10)]

for n in S[1:]:
    right[n] += 1
left[S[0]] = True
flag = [[[False for i in range(10)] for j in range(10)] for k in range(10)]
for n in S[1:-1]:
    right[n] -= 1
    for i, l in enumerate(left):
        if l:
            for j, r in enumerate(right):
                if r > 0:
                    flag[n][i][j] = True
    left[n] = True
count = 0
for i in flag:
    for j in i:
        for k in j:
            if k:
                count += 1
print(count)
