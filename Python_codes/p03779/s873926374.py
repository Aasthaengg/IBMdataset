x = int(input())
ans = 0
num = 0
while True:
    if x<=num:
        break
    ans += 1
    num += ans
print(ans)