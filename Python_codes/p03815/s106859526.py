x = int(input())
X = x % 11
N = x // 11

ans = 0
if 1 <= X <= 6:
    ans = N*2 + 1
elif 7 <= X <= 10:
    ans = N*2 + 2
else:
    ans = N*2

print(ans)
