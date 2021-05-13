
N = int(input())
S = input()

count_W = []
count = 0
for i in range(N):
    if i == 0:
        count_W.append(0)
    else:
        if S[i-1:i] == 'W':
            count += 1
        count_W.append(count)

count_E = []
for i in range(N):
    count_E.append(0)
count = 0
for i in range(N - 1, -1, -1):
    if S[i+1:i+2] == 'E':
        count += 1
    count_E[i] = count

total_list = []
for i in range(N):
    to_E = count_W[i]
    to_W = count_E[i]
    total_list.append(to_E + to_W)

print(min(total_list))
