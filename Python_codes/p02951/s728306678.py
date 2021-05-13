a,b,c = map(int, input().split())
hairu = a-b
nokoru = 0
if hairu == 0:
    nokoru += c
elif hairu > c:
    nokoru = 0
else:
    nokoru += c- hairu
print(nokoru)