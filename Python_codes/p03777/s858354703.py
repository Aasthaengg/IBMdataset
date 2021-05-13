a, b = input().split()

if a == "H":
    if b == "D":
        ans = "D"
    else:
        ans = "H"
else:
    if b == "D":
        ans = "H"
    else:
        ans = "D"

print(ans)