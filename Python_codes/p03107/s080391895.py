s = input()

ans = 0
ind = 0
while ind < len(s)-1:
    if s[ind:ind+2] in ("01", "10"):
        s = s[:ind]+s[ind+2:]
        ans += 1
        ind = max(0, ind-1)

    else:
        ind += 1
print(ans*2)
