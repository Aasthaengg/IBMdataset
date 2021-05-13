s=str(input())
a="Y"
b="Y"
if 0<int(s[0:2])<13:
    a="MY"
if 0<int(s[2:5])<13:
    b="MY"

if a==b=="Y":
    ans="NA"
elif a=="Y" and b=="MY":
    ans="YYMM"
elif a=="MY" and b=="Y":
    ans="MMYY"
else:
    ans="AMBIGUOUS"
print(ans)