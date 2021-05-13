R = int(input())

ans = ""
if R < 1200:
    ans = "ABC"
elif 1200 <= R < 2800:
    ans = "ARC"
else:
    ans = "AGC"

print(ans)