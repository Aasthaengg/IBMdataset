s = list(input())
k = int(input())
ans = "1"
cnt = 0
for i in s:
    if i == "1":
        cnt += 1
    elif cnt < k:
        ans = str(i)
        break
print(ans)
