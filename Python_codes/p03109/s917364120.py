s = input()
s1 = s.split("/")

ans = "Heisei"
if int(s1[0]) >= 2019:
    if int(s1[1]) >= 5:
        ans = "TBD"

print(ans)
