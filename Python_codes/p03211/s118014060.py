s = input()

ans = float("inf")
for i in range(len(s)-2):
    num = int(s[i:i+3])
    if abs(753-num) < ans:
        ans = abs(753-num)

print(ans)