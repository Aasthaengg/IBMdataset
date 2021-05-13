x = list(input())
y = len(x)
for i in range(y):
    if x[i] == "1":
        x[i] = "9"
    else:
        x[i] = "1"

print(int("".join(x)))
