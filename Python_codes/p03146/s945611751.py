s = int(input())
visited = set()
count = 0

while True:
    count += 1
    if s in visited:
        break
    else:
        visited.add(s)
        if s%2 == 0:
            s = s//2
        else:
            s = 3*s+1

print(count)