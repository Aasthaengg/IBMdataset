x, y = map(int, input().split(" "))

if y % 2 != 0:
    ans = "No"
elif (y >= 2*x) and (y <= 4*x):
    ans = "Yes"
else:
    ans = "No"

print(ans)