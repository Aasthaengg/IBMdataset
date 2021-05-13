n = int(input())
l = []
if n%2:
    for i in range(1,n):
        for j in range(i+1,n+1):
            if i+j == n:
                continue
            l.append([i,j])
else:
    for i in range(1,n):
        for j in range(i+1,n+1):
            if i+j == n+1:
                continue
            l.append([i,j])
print(len(l))
for i in l:
    print(*i)
