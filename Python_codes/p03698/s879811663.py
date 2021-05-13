S = input()

a = []
result = "yes"
for s in S:
    if s in a:
        result = "no"
        break
    a.append(s)

print(result)