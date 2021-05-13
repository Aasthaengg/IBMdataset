X = int(input())

ans = 0
check = 0
for i in range(1, 10**7):
    ans += i
    check += 1
    if X <= ans:
        print(check)
        break