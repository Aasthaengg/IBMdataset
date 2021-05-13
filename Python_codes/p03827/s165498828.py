n = int(input())
s = input()

ans = 0
ans_max = 0
for i in s:
    if i == "I":
        ans += 1
    else:
        ans -= 1
    if ans > ans_max:
        ans_max = ans

print(ans_max)