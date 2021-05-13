x = list(input())
count = 0
for i in range(4):
    if x[i] == "+":
        count += 1
    else:
        count -= 1
print(count)
