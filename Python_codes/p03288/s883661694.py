r = int(input())
ans = "AGC"
if r < 1200:
    ans = "ABC"
elif r < 2800:
    ans = "ARC"
print(ans)