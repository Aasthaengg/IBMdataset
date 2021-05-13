r = int(input())
ans = ""

if r < 1200:
    ans = "ABC"

elif r >=1200 and r < 2800:
    ans = "ARC"

else:
    ans = "AGC"

print(ans)