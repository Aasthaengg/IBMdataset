n = input()
ans = 0
for i in range(len(n)):
    if n[i:i+1] == "2":
        ans += 1
print(ans)