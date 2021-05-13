N = int(input())
A = list(map(int, input().split()))
box = [0] * (N+1)
M = 0
ans = []

for i in range(N, 0, -1):
    tmp = 0
    for j in range(i*2, N+1, i):
        tmp += box[j]
    tmp = tmp % 2
    if tmp != A[i-1]:
        box[i] = 1
        M += 1
        ans.append(i)

if M == 0:
    print(0)
else:
    ans = ans[::-1]
    print(M)
    print(*ans)
