s = input()
s2 = ""
for i in s:
    if i != "x":
        s2 += i
if s2 != s2[::-1]:
    print(-1)
else:
    temp = s2[:(len(s2) + 1) // 2]
    ans = 0
    num1 = 0
    num2 = len(s) - 1
    for i in range(len(temp)):
        count1 = 0
        while s[num1] != temp[i]:
            count1 += 1
            num1 += 1
        else:
            num1 += 1
        count2 = 0
        while s[num2] != temp[i]:
            count2 += 1
            num2 -= 1
        else:
            num2 -= 1
        ans += abs(count1 - count2)
    print(ans)