S = input()
s = S[::-1]
a = "dream"[::-1]
b = "dreamer"[::-1]
c = "erase"[::-1]
d = "eraser"[::-1]

idx = 0
ans = "YES"
while idx < len(s):
    if s[idx] == "m":
        if s[idx : idx + 5] == a:
            idx = idx + 5
        else:
            ans = "NO"
            break

    elif s[idx] == "e":
        if s[idx : idx + 5] == c:
            idx = idx + 5
        else:
            ans = "NO"
            break

    elif s[idx] == "r":
        if s[idx : idx + 7] == b:
            idx = idx + 7
        elif s[idx : idx + 6] == d:
            idx = idx + 6
        else:
            ans = "NO"
            break

    else:
        ans = "NO"
        break

print(ans)