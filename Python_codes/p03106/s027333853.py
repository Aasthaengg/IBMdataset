a,b,k = map(int,input().split())
c = 0
i = max(a,b)

while i > 0:
    if a % i == 0:
        if b % i == 0:
            c += 1

    if c == k:
        print(i)
        break

    i -= 1