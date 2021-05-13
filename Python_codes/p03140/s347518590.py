n,a,b,c = [input() for i in range(4)]
counter = 0
for i in range(int(n)):
    if a[i] == b[i] != c[i]:
        counter += 1
    elif a[i] == c[i] != b[i]:
        counter += 1
    elif a[i] != b[i] == c[i]:
        counter += 1
    elif a[i] != b[i] != c[i]:
        counter += 2
print(counter)