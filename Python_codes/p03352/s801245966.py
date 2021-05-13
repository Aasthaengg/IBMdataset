x = int(input())
k = 0

for i in range(1,1000):
    for j in range(2,1000):
        if i ** j <= x:
            k = max(k,i ** j)
        else:
            break
    if x // 2 < i:
        break

print(k)