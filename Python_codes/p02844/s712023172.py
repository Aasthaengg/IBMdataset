
N = int(input())
S = list(input())

count = 0
for N in range(1000):
    password = list(f"{N:03d}")
    i = 0
    p = password[i]
    for x in S:
        if x == p:
            if i < 2:
                i += 1
                p = password[i]
            else:
                count += 1
                break

print(count)
