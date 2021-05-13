N = int(input())
H = list(map(int, input().split()))
max_h = H[0]
flag = 0

for i in range(1, N):
    max_h = max(max_h, H[i])
    if max_h - H[i] > 1:
        flag += 1

if flag:
    print('No')
else:
    print('Yes')
