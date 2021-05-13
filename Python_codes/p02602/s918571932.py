N, K = map(int, input().split())
a = list(map(int, input().split()))

ans = []
flag = 1
for i in range(N):
    if a[i] < a[i + K]:
        print('Yes')
    else:
        print("No")
    flag += 1
    if flag == N-K+1:
        break