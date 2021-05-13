s = str(input())
ans = 0
correct_list = list("CODEFESTIVAL2016")
for i in range(0,16):
    if s[i] != correct_list[i]:
        ans += 1
print(ans)
