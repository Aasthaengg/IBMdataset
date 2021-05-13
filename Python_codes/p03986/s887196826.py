X = input()
N = len(X)

right = 1
cnt = 0

for left in range(N - 1):
    if X[left] == 'S':
        right = max(right, left + 1)
        while right < N and X[right] != 'T':
            right += 1
        if right >= N:
            break
        if X[right] == 'T':
            # print(left, right)
            right += 1
            cnt += 1
print(N - cnt * 2)