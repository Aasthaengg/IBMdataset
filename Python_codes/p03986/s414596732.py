x = input()
depth = 0
min_depth = 0
for char in x:
    if char == 'T':
        depth -= 1
        if depth < min_depth:
            min_depth = depth
    else:
        depth += 1
print(-2*min_depth-depth)