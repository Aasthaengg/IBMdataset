N = int(input())
A = sorted(list(map(int, input().split())))

ans = 1
for i in A:
    ans *= i
    if ans > pow(10, 18):
        ans = -1
        break
print(ans)