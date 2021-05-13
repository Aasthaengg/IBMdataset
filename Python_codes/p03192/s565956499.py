N = str(input())
ans = 0
for i in range(4):
    if N[i] == "2":
        ans += 1
    else:
        ans += 0
print(ans)