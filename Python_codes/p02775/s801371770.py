n = input()
precise = 0
over = 1
for d in n:
    d = int(d)
    new_over = min(precise + d + 1, over + d + 2, over + 9 - d)
    precise = min(over + d + 1, precise + d)
    over = new_over
over += 1
print(min(precise, over))
