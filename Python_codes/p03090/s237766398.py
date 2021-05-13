n = int(input())
r = []
if n%2==0:
    c = 1
else: 
    c = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        if n-i+c == j:
            continue
        else:
            r.append([i, j])
print(len(r))
for i in r:
    print(*i)