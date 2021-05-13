S = input()
c = 0
current_B_counter = 0
for s in S:
    if s == "B":
        current_B_counter += 1
    if s == "W":
        c += current_B_counter

print(c)