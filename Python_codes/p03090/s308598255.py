n = int(input())
e = []
if n % 2 == 0:
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if i + j == n + 1:
                continue
            e.append([i, j])
else:
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if i + j == n:
                continue
            e.append([i, j])
print(len(e))
for i in e:
    print(i[0],i[1])