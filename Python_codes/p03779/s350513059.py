N = int(input())

ans = 0
sum = 0

for i in range(1, 10**9):
    sum += i
    ans += 1
    if sum >= N:
        print(ans)
        exit()