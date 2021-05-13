r, D, x = map(int, input().split())

ans = [None]*11
ans[0] = x

for i in range(1, 11):
    ans[i] = ans[i-1] * r - D
    print(ans[i])