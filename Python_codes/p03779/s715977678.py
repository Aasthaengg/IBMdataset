x = int(input())
reached, ans = 0, 0
while reached < x:
    reached += ans
    if reached >= x:
        break
    ans += 1
    # print(reached, ans)
print(ans)