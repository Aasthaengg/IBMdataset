N = int(input())
a = []
 
for x in range(1, N):
    y = N-x
    if x == y:
        continue
    if x > y:
        break
    a.append([x, y])
 
print(len(a))