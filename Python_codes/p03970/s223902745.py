s = input()
count = 0
check = "CODEFESTIVAL2016"
for i in range(len(s)):
    if s[i] != check[i]:
        count += 1
print(count)