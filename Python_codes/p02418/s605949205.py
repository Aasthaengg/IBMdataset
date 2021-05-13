ring = input()
s = input()
result = 'No'
for i in range(len(ring)):
    if s in ring:
        result = 'Yes'
        break
    ring = ring[1:] + ring[0]
print(result)
