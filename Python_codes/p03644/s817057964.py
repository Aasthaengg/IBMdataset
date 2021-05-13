N = int(input())

ans_list = [1, 2, 4, 8, 16, 32, 64]

for n in ans_list:
    if (n <= N):
        ans = n

print(ans)