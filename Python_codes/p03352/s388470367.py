X = int(input())

ans = 0

for i in range(2, 9 + 1):
    for j in range(1, 1000 + 1):
        ans_ = j ** i
        ans = max(ans, ans_) if ans_ <= X else ans

print(ans)