N = int(input())
S = list(input())
x = 0
ans = 0
for i in S:
    if i == "I":
        x += 1
    else:
        x -= 1
    ans = max(ans, x)
print(ans)
