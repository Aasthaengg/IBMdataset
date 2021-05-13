days = input()

day1 = days[0]
day2 = days[1]
day3 = days[2]

ans = 0

if day1 == "R":
    ans += 1
    if day2 == "R":
        ans += 1
        if day3 == "R":
            ans +=1
elif day2 == "R":
    ans += 1
    if day3 == "R":
         ans +=1

elif day3 == "R":
    ans +=1

print(ans)