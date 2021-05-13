n = int(input())

type1 = type2 = type3 = 0

ans = 0
while n > 0:
    s = input()
    ans += s.count("AB")

    if s[0] == "B" and s[-1] == "A":
        type3 += 1
    elif s[-1] == "A":
        type1 += 1
    elif s[0] == "B":
        type2 += 1

    n -= 1

ans += min(type1, type2)

if type3 > 0:
    if type1 == type2 == 0:
        ans += type3 - 1
    else:
        ans += type3

print(ans)
