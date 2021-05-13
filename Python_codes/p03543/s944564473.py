N = input()

ans = "No"
for i in range(10):
    if N[:3].count(str(i)) == 3 or N[1:4].count(str(i)) == 3:
        ans = "Yes"

print(ans)