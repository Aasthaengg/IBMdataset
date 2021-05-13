R = int(input())

res = "AGC"
if R < 1200:
    res = "ABC"
if 1200 <= R < 2800:
    res = "ARC"
print(res)