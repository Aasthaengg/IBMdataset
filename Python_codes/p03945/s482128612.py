S = input()
result = -1
piyo = ""
for s in S:
    if piyo != s:
        piyo = s
        result += 1
print(result)
