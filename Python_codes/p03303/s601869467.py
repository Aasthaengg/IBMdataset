strin = str(input())
w = int(input())
ans = ""
for i in range(len(strin)):
    if i%w == 0:
        ans += strin[i]

print(ans)