n = int(input())
s = input()
x = 0
result = x
for c in s:
    if c == "I":
        x += 1
    else:
        x -= 1
    result = max(result, x)
print(result)