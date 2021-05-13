s = list(input())
ans = 0
cnt =0
for i in s:
    if i == "B":
        cnt += 1
    else:
        ans += cnt
print(ans)