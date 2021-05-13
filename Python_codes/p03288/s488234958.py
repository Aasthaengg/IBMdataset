r = int(input())
s = ""
if r < 1200:
    s = "ABC"
elif r < 2800:
    s = "ARC"
else:
    s = "AGC"
print(s)