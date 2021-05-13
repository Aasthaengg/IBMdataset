n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(set(a))
count = 0
z = 0
for i in b:
    if i > n:
        count += n-z
        break
    else:
        j = a.count(i)
        if j < i:
            count += j
            z += j
        else:
            count += j-i
            z += j
print(count)