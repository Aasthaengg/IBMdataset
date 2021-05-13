A, B = map(int, input().split())

if B == 1:
    print(0)
    exit()

ans = 0
while (A + (A - 1) * ans) < B:
    ans += 1

print(ans+1)