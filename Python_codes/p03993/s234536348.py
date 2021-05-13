N = int(input())
A = [x - 1 for x in map(int, input().split())]

cnt = 0
for i in range(N):
    if A[A[i]] == i:
        cnt += 1
print(cnt // 2)

