N, x = map(int, input().split())
children = sorted(list(map(int, input().split())))

count = 0
for child in children:
    if x >= child:
        x -= child
        count += 1
    else:
        break
else:
    if x != 0:
        count -= 1

print(count)