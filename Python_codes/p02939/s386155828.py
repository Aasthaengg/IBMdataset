S = input()
result = 0
now = S[0]
temp = ""
for s in S[1:]:
    temp += s
    if now == temp:
        continue
    else:
        result += 1
        now = temp
        temp = ""
print(result + 1)
