s = input()

counter = 0
max_counter = 0
for c in s:
    if c in 'ACGT':
        counter += 1
    else:
        counter = 0
    if max_counter < counter:
        max_counter = counter
print(max_counter)