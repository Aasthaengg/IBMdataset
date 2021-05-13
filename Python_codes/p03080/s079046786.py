n = int(input())
s = input()

red = s.count("R")
if red > n - red:
    ans = "Yes"
else:
    ans = "No"
print(ans)
