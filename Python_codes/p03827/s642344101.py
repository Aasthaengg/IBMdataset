n = int(input())
s = input()

ans = 0
tmp = 0
for i in s:
    if i == "I": tmp += 1
    if i == "D": tmp -= 1
    ans = max(ans, tmp)

print(ans)