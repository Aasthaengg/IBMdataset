#conding-utf-8
R=int(input())
ans="unnamed"
if R<1200:
    ans="ABC"
elif 1200<=R<2800:
    ans="ARC"
elif 2800<=R:
    ans="AGC"

print(ans)
