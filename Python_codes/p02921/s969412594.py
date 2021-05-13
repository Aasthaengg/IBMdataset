Pre = input()
Truth = input()
count = 0
for a,b in zip(Pre,Truth):
    if a == b:
        count += 1
print(count)