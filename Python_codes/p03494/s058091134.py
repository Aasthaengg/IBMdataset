N = int(input())
A = list(map(int, input().split()))

cnt = 0
while True: 
    odd_flag = False
    for i in range(N):
        if A[i] % 2 == 1:
            odd_flag = True
    if odd_flag:
        break
    for i in range(N):
        A[i] = A[i] // 2
    cnt += 1

print(cnt)