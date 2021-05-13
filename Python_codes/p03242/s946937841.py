n = list(input())
ans = ""
for s in n:
    if s == "9":
        ans += "1"
        continue

    if s == "1":
        ans += "9"
        continue

    ans += s
    
print(ans)
