N, K = map(int, input().split())
h = tuple(map(int, input().split()))
counter = 0
for person_height in h:
    if person_height >= K:
        counter += 1
print(counter)
