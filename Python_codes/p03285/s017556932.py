n = int(input())
ans = "No"
for i in range(26):
    for j in range(20):
        if 4*i+7*j==n:
            ans = "Yes"
            break
print(ans)