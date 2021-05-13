s = input()
w_num = s.count("W")
ans = 0
for i in s:
    if i == "B":
        ans += w_num
    else:
        w_num -= 1
print(ans)