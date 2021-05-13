N, M = map(int, input().split())
A = ['' for _ in range(N)]
B = ['' for _ in range(N)]
for i in range(N):
    A[i] = input()
for i in range(M):
    B[i] = input()

H = N - M + 1
flag = 'No'

for i in range(H):
    for j in range(H):
        cnt = 0
        for d in range(M):
            if B[d] != A[i+d][j:j+M]:
                break
            cnt += 1
        if cnt == M:
            flag = 'Yes'
            break
    else:
        continue
    break

print(flag)