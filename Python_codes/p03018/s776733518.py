S = input()
S = S.replace("BC", "D")
result = 0
temp = 0
for s in S:
    if s == "A":
        temp += 1
    elif s == "D":
        result += temp
    else:
        temp = 0
print(result)