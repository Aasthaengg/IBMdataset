n = int(input())
ans = 111

for i in range(9):
    if n <= ans:
        print(ans)
        exit()
    else:
        ans += 111