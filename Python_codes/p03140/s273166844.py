N = int(input())
a = list(input())
b = list(input())
c = list(input())
count = 0
for i in range(N):
    if a[i]==b[i] or b[i]==c[i] or c[i]==a[i]:
        if a[i]==b[i] and b[i]==c[i]:
            continue
        else:
            count += 1
    else:
        count += 2
print(count)