red, green, blue = map(int, input().split())
k = int(input())
ans = "No"

for _ in range(k):
    if green <= red:
        green *= 2
    else:
        if blue <= green:
            blue *= 2
        else:
            break
if blue > green > red:
    ans = "Yes"
print(ans)